const fs = require('fs');
const path = require('path');

class Parser {
  constructor(file) {
    this.file = file;
  }

  async parse() {
    try {
      const data = await fs.promises.readFile(this.file, 'utf8');
      const terraformConfig = JSON.parse(data);
      return terraformConfig;
    } catch (error) {
      throw new Error(`Error parsing file: ${error.message}`);
    }
  }

  isValidTerraformConfig(config) {
    if (!config || typeof config !== 'object') {
      return false;
    }
    const requiredProperties = ['provider', 'resource'];
    return requiredProperties.every(property => property in config);
  }
}

module.exports = Parser;