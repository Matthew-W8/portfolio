<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="xs math"
    version="3.0">
    
    
    <xsl:mode on-no-match="shallow-copy"/>
    
    <xsl:template match="text()">
        
        <!-- This Regex works really well, but I can't get it to verify because of the tag. -->
        <xsl:analyze-string select="." regex="<sp>(\w.+?)[\[|:]" flags="s">
            <!-- Attempting to find all names by looking for the <sp> tag and the searching until a ':' or '[' -->
            <xsl:matching-substring>
                <name><xsl:value-of select="regex-group(1)"/></name>
            </xsl:matching-substring>
  
            <xsl:non-matching-substring>
                <xsl:apply-templates select="."/>
            </xsl:non-matching-substring>
            
        </xsl:analyze-string>
    </xsl:template>
    
</xsl:stylesheet>