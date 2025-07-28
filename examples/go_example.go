package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
	"time"
)

// AvatarGenerator 头像生成器客户端
type AvatarGenerator struct {
	BaseURL string
	Client  *http.Client
}

// GenerateRequest 生成请求参数
type GenerateRequest struct {
	Size   int    `json:"size"`
	Gender string `json:"gender"`
}

// SaveRequest 保存请求参数
type SaveRequest struct {
	Size     int    `json:"size"`
	Gender   string `json:"gender"`
	Format   string `json:"format"`
	Filename string `json:"filename"`
}

// BatchSaveRequest 批量保存请求参数
type BatchSaveRequest struct {
	Amount int    `json:"amount"`
	Size   int    `json:"size"`
	Gender string `json:"gender"`
	Format string `json:"format"`
}

// AvatarResponse 头像响应
type AvatarResponse struct {
	Success bool `json:"success"`
	Data    struct {
		SVG    string `json:"svg"`
		Size   int    `json:"size"`
		Gender string `json:"gender"`
	} `json:"data"`
	Error string `json:"error,omitempty"`
}

// NewAvatarGenerator 创建新的头像生成器
func NewAvatarGenerator(baseURL string) *AvatarGenerator {
	if baseURL == "" {
		baseURL = "https://api.binrc.com"
	}
	return &AvatarGenerator{
		BaseURL: baseURL,
		Client:  &http.Client{Timeout: 30 * time.Second},
	}
}

// GenerateAvatar 生成单个头像
func (ag *AvatarGenerator) GenerateAvatar(size int, gender string) (*AvatarResponse, error) {
	reqBody := GenerateRequest{
		Size:   size,
		Gender: gender,
	}

	jsonData, err := json.Marshal(reqBody)
	if err != nil {
		return nil, fmt.Errorf("marshal request failed: %v", err)
	}

	resp, err := ag.Client.Post(ag.BaseURL+"/avatar/generate", "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		return nil, fmt.Errorf("request failed: %v", err)
	}
	defer resp.Body.Close()

	var result AvatarResponse
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return nil, fmt.Errorf("decode response failed: %v", err)
	}

	return &result, nil
}

// SaveAvatar 保存头像文件
func (ag *AvatarGenerator) SaveAvatar(size int, gender, format, filename string) error {
	if filename == "" {
		filename = fmt.Sprintf("avatar_%d", time.Now().Unix())
	}

	reqBody := SaveRequest{
		Size:     size,
		Gender:   gender,
		Format:   format,
		Filename: filename,
	}

	jsonData, err := json.Marshal(reqBody)
	if err != nil {
		return fmt.Errorf("marshal request failed: %v", err)
	}

	resp, err := ag.Client.Post(ag.BaseURL+"/avatar/save", "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		return fmt.Errorf("request failed: %v", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		body, _ := io.ReadAll(resp.Body)
		return fmt.Errorf("save failed with status %d: %s", resp.StatusCode, string(body))
	}

	// 保存文件
	file, err := os.Create(fmt.Sprintf("%s.%s", filename, format))
	if err != nil {
		return fmt.Errorf("create file failed: %v", err)
	}
	defer file.Close()

	_, err = io.Copy(file, resp.Body)
	if err != nil {
		return fmt.Errorf("write file failed: %v", err)
	}

	fmt.Printf("✅ %s头像已保存: %s.%s\n", strings.ToUpper(format), filename, format)
	return nil
}

// BatchSaveAvatars 批量保存头像
func (ag *AvatarGenerator) BatchSaveAvatars(amount, size int, gender, format string) error {
	reqBody := BatchSaveRequest{
		Amount: amount,
		Size:   size,
		Gender: gender,
		Format: format,
	}

	jsonData, err := json.Marshal(reqBody)
	if err != nil {
		return fmt.Errorf("marshal request failed: %v", err)
	}

	resp, err := ag.Client.Post(ag.BaseURL+"/avatar/save/batch", "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		return fmt.Errorf("request failed: %v", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		body, _ := io.ReadAll(resp.Body)
		return fmt.Errorf("batch save failed with status %d: %s", resp.StatusCode, string(body))
	}

	// 保存ZIP文件
	filename := fmt.Sprintf("avatars_%s_%d.zip", format, time.Now().Unix())
	file, err := os.Create(filename)
	if err != nil {
		return fmt.Errorf("create file failed: %v", err)
	}
	defer file.Close()

	_, err = io.Copy(file, resp.Body)
	if err != nil {
		return fmt.Errorf("write file failed: %v", err)
	}

	fmt.Printf("✅ 批量%s头像已保存: %s\n", strings.ToUpper(format), filename)
	return nil
}

// GetAvatarJSON 获取头像JSON数据
func (ag *AvatarGenerator) GetAvatarJSON(size int, gender string) (*AvatarResponse, error) {
	url := fmt.Sprintf("%s/avatar/json?size=%d&gender=%s", ag.BaseURL, size, gender)

	resp, err := ag.Client.Get(url)
	if err != nil {
		return nil, fmt.Errorf("request failed: %v", err)
	}
	defer resp.Body.Close()

	var result AvatarResponse
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return nil, fmt.Errorf("decode response failed: %v", err)
	}

	return &result, nil
}

// TestAPI 测试API连接
func (ag *AvatarGenerator) TestAPI() error {
	resp, err := ag.Client.Get(ag.BaseURL + "/test")
	if err != nil {
		return fmt.Errorf("test request failed: %v", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return fmt.Errorf("test failed with status %d", resp.StatusCode)
	}

	body, _ := io.ReadAll(resp.Body)
	fmt.Printf("✅ API测试成功: %s\n", string(body))
	return nil
}

func main() {
	fmt.Println("🎨 AvatarPyCor Golang 使用示例")
	fmt.Println("================================")

	// 初始化客户端
	generator := NewAvatarGenerator("")

	// 测试API连接
	fmt.Println("\n0️⃣ 测试API连接:")
	if err := generator.TestAPI(); err != nil {
		fmt.Printf("❌ API测试失败: %v\n", err)
		return
	}

	// 1. 生成单个头像
	fmt.Println("\n1️⃣ 生成单个头像:")
	result, err := generator.GenerateAvatar(300, "1") // 300x300 男性头像
	if err != nil {
		fmt.Printf("❌ 生成失败: %v\n", err)
	} else if result.Success {
		fmt.Println("✅ 头像生成成功")
		fmt.Printf("📏 尺寸: %d\n", result.Data.Size)
		fmt.Printf("👤 性别: %s\n", result.Data.Gender)
		fmt.Printf("📄 SVG长度: %d 字符\n", len(result.Data.SVG))
	} else {
		fmt.Printf("❌ 生成失败: %s\n", result.Error)
	}

	// 2. 保存SVG头像
	fmt.Println("\n2️⃣ 保存SVG头像:")
	if err := generator.SaveAvatar(280, "2", "svg", "female_avatar"); err != nil {
		fmt.Printf("❌ 保存失败: %v\n", err)
	}

	// 3. 保存PNG头像
	fmt.Println("\n3️⃣ 保存PNG头像:")
	if err := generator.SaveAvatar(400, "0", "png", "random_avatar"); err != nil {
		fmt.Printf("❌ 保存失败: %v\n", err)
	}

	// 4. 批量保存SVG头像
	fmt.Println("\n4️⃣ 批量保存SVG头像:")
	if err := generator.BatchSaveAvatars(3, 200, "1", "svg"); err != nil {
		fmt.Printf("❌ 批量保存失败: %v\n", err)
	}

	// 5. 批量保存PNG头像
	fmt.Println("\n5️⃣ 批量保存PNG头像:")
	if err := generator.BatchSaveAvatars(2, 300, "2", "png"); err != nil {
		fmt.Printf("❌ 批量保存失败: %v\n", err)
	}

	// 6. 获取JSON数据
	fmt.Println("\n6️⃣ 获取头像JSON数据:")
	jsonResult, err := generator.GetAvatarJSON(250, "0")
	if err != nil {
		fmt.Printf("❌ 获取失败: %v\n", err)
	} else if jsonResult.Success {
		fmt.Println("✅ JSON数据获取成功")
		fmt.Printf("📏 尺寸: %d\n", jsonResult.Data.Size)
		fmt.Printf("👤 性别: %s\n", jsonResult.Data.Gender)
	} else {
		fmt.Printf("❌ 获取失败: %s\n", jsonResult.Error)
	}

	fmt.Println("\n🎉 示例运行完成！")

	// 列出生成的文件
	fmt.Println("\n📋 生成的文件:")
	files, err := os.ReadDir(".")
	if err == nil {
		for _, file := range files {
			if !file.IsDir() {
				name := file.Name()
				if strings.HasSuffix(name, ".svg") || strings.HasSuffix(name, ".png") || strings.HasSuffix(name, ".zip") {
					info, _ := file.Info()
					fmt.Printf("  %s (%d bytes)\n", name, info.Size())
				}
			}
		}
	}
}
