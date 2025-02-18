<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    xmlns:xd="http://www.oxygenxml.com/ns/doc/xsl"
    exclude-result-prefixes="xs math xd"
    version="3.0">
    <xsl:mode on-no-match="shallow-copy"/>
    <xsl:template match="text()">
        <xsl:analyze-string select="." regex="CHAPTER\s[IVX]+" flags="s">
            <xsl:matching-substring>
                <chapter><xsl:value-of select="regex-group(0)"/></chapter>
            </xsl:matching-substring>
        </xsl:analyze-string>
    </xsl:template>
    
    <xsl:template match="text()">
        <xsl:analyze-string select="." regex="^[\d\D]+?\n" flags="s">
            <xsl:matching-substring>
                <p><xsl:value-of select="regex-group(0)"/></p>
            </xsl:matching-substring>
        </xsl:analyze-string>
    </xsl:template>
    <!-- I wasn't sure what passages was suppossed to mean -->
    
    <xsl:template match="text()">
        <xsl:analyze-string select="." regex="(\d+\s[\w]+?)\." flags="s">
            <xsl:matching-substring>
                <date><xsl:value-of select="regex-group(0)"/></date>
            </xsl:matching-substring>
        </xsl:analyze-string>
    </xsl:template>
    <!-- I don't know what was going wrong with my regex but it kept returning an error saying was taking too long to run -->
    
    <!-- I just couldn't seem to find any letters in the text -->
    
</xsl:stylesheet>