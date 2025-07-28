/**
 * AvatarPyCor JavaScript 使用示例
 */

class AvatarGenerator {
    constructor(baseUrl = 'https://api.binrc.com') {
        this.baseUrl = baseUrl.replace(/\/$/, '');
    }

    /**
     * 生成单个头像
     * @param {number} size - 头像尺寸
     * @param {string} gender - 性别 ('0': 随机, '1': 男性, '2': 女性)
     * @returns {Promise<Object>}
     */
    async generateAvatar(size = 280, gender = '0') {
        const response = await fetch(`${this.baseUrl}/avatar/generate`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ size, gender })
        });
        return await response.json();
    }

    /**
     * 保存SVG头像
     * @param {number} size - 头像尺寸
     * @param {string} gender - 性别
     * @param {string} filename - 文件名
     * @returns {Promise<boolean>}
     */
    async saveAvatarSVG(size = 280, gender = '0', filename = null) {
        const response = await fetch(`${this.baseUrl}/avatar/save`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                size,
                gender,
                format: 'svg',
                filename: filename || `avatar_${Date.now()}`
            })
        });

        if (response.ok) {
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `${filename || `avatar_${Date.now()}`}.svg`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
            console.log(`✅ SVG头像已下载: ${a.download}`);
            return true;
        } else {
            const error = await response.text();
            console.error(`❌ 保存失败: ${error}`);
            return false;
        }
    }

    /**
     * 保存PNG头像
     * @param {number} size - 头像尺寸
     * @param {string} gender - 性别
     * @param {string} filename - 文件名
     * @returns {Promise<boolean>}
     */
    async saveAvatarPNG(size = 280, gender = '0', filename = null) {
        const response = await fetch(`${this.baseUrl}/avatar/save`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                size,
                gender,
                format: 'png',
                filename: filename || `avatar_${Date.now()}`
            })
        });

        if (response.ok) {
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `${filename || `avatar_${Date.now()}`}.png`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
            console.log(`✅ PNG头像已下载: ${a.download}`);
            return true;
        } else {
            const error = await response.text();
            console.error(`❌ 保存失败: ${error}`);
            return false;
        }
    }

    /**
     * 批量保存头像
     * @param {number} amount - 数量
     * @param {number} size - 头像尺寸
     * @param {string} gender - 性别
     * @param {string} format - 格式 ('svg' 或 'png')
     * @returns {Promise<boolean>}
     */
    async batchSaveAvatars(amount = 5, size = 280, gender = '0', format = 'svg') {
        const response = await fetch(`${this.baseUrl}/avatar/save/batch`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                amount,
                size,
                gender,
                format
            })
        });

        if (response.ok) {
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `avatars_${format}_${Date.now()}.zip`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
            console.log(`✅ 批量头像已下载: ${a.download}`);
            return true;
        } else {
            const error = await response.text();
            console.error(`❌ 批量保存失败: ${error}`);
            return false;
        }
    }

    /**
     * 获取头像JSON数据
     * @param {number} size - 头像尺寸
     * @param {string} gender - 性别
     * @returns {Promise<Object>}
     */
    async getAvatarJSON(size = 280, gender = '0') {
        const response = await fetch(`${this.baseUrl}/avatar/json?size=${size}&gender=${gender}`);
        return await response.json();
    }

    /**
     * 在页面上显示头像
     * @param {string} svgContent - SVG内容
     * @param {string} containerId - 容器ID
     */
    displayAvatar(svgContent, containerId = 'avatar-container') {
        const container = document.getElementById(containerId);
        if (container) {
            container.innerHTML = svgContent;
        } else {
            console.error(`❌ 容器未找到: ${containerId}`);
        }
    }
}

// 使用示例
async function main() {
    console.log('🎨 AvatarPyCor JavaScript 使用示例');
    console.log('='.repeat(50));

    const generator = new AvatarGenerator();

    try {
        // 1. 生成单个头像
        console.log('\n1️⃣ 生成单个头像:');
        const result = await generator.generateAvatar(300, '1'); // 300x300 男性头像
        if (result.success) {
            console.log('✅ 头像生成成功');
            console.log(`📏 尺寸: ${result.data.size}`);
            console.log(`👤 性别: ${result.data.gender}`);
            console.log(`📄 SVG长度: ${result.data.svg.length} 字符`);

            // 在页面上显示头像
            generator.displayAvatar(result.data.svg, 'avatar-display');
        } else {
            console.log(`❌ 生成失败: ${result.error}`);
        }

        // 2. 保存SVG头像
        console.log('\n2️⃣ 保存SVG头像:');
        await generator.saveAvatarSVG(280, '2', 'female_avatar'); // 女性头像

        // 3. 保存PNG头像
        console.log('\n3️⃣ 保存PNG头像:');
        await generator.saveAvatarPNG(400, '0', 'random_avatar'); // 随机头像

        // 4. 批量保存SVG头像
        console.log('\n4️⃣ 批量保存SVG头像:');
        await generator.batchSaveAvatars(3, 200, '1', 'svg'); // 3个男性头像

        // 5. 批量保存PNG头像
        console.log('\n5️⃣ 批量保存PNG头像:');
        await generator.batchSaveAvatars(2, 300, '2', 'png'); // 2个女性头像

        // 6. 获取JSON数据
        console.log('\n6️⃣ 获取头像JSON数据:');
        const jsonResult = await generator.getAvatarJSON(250, '0');
        if (jsonResult.success) {
            console.log('✅ JSON数据获取成功');
            console.log(`📏 尺寸: ${jsonResult.data.size}`);
            console.log(`👤 性别: ${jsonResult.data.gender}`);
        } else {
            console.log(`❌ 获取失败: ${jsonResult.error}`);
        }

        console.log('\n🎉 示例运行完成！');

    } catch (error) {
        console.error('❌ 运行出错:', error);
    }
}

// 浏览器环境下的使用示例
if (typeof window !== 'undefined') {
    // 创建示例HTML
    const html = `
        <!DOCTYPE html>
        <html>
        <head>
            <title>AvatarPyCor 示例</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                .avatar-display { border: 1px solid #ccc; padding: 10px; margin: 10px 0; }
                button { margin: 5px; padding: 10px; cursor: pointer; }
            </style>
        </head>
        <body>
            <h1>🎨 AvatarPyCor JavaScript 示例</h1>
            <div>
                <button onclick="generateRandom()">生成随机头像</button>
                <button onclick="saveSVG()">保存SVG</button>
                <button onclick="savePNG()">保存PNG</button>
                <button onclick="batchSave()">批量保存</button>
            </div>
            <div id="avatar-display" class="avatar-display">
                <p>头像将在这里显示...</p>
            </div>
            <script src="javascript_example.js"></script>
            <script>
                const generator = new AvatarGenerator();
                
                async function generateRandom() {
                    const result = await generator.generateAvatar(300, '0');
                    if (result.success) {
                        generator.displayAvatar(result.data.svg, 'avatar-display');
                    }
                }
                
                async function saveSVG() {
                    await generator.saveAvatarSVG(300, '0', 'my_avatar');
                }
                
                async function savePNG() {
                    await generator.saveAvatarPNG(300, '0', 'my_avatar');
                }
                
                async function batchSave() {
                    await generator.batchSaveAvatars(5, 300, '0', 'svg');
                }
            </script>
        </body>
        </html>
    `;

    // 在Node.js环境中，可以导出类
    if (typeof module !== 'undefined' && module.exports) {
        module.exports = AvatarGenerator;
    }
}

// 如果直接运行此文件
if (typeof require !== 'undefined' && require.main === module) {
    main();
} 