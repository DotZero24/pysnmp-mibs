_N='colubrisVscMIBGroup'
_M='coVscCfgHTMLAuthentication'
_L='coVscCfgMACAuthentication'
_K='coVscCfg8021xAuthentication'
_J='coVscCfgEncryption'
_I='coVscCfgSecurity'
_H='coVscCfgAccessControlled'
_G='coVscCfgSSID'
_F='coVscCfgFriendlyVscName'
_E='coVscCfgIndex'
_D='Integer32'
_C='read-only'
_B='COLUBRIS-VSC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
colubrisMgmtV2,=mibBuilder.importSymbols('COLUBRIS-SMI','colubrisMgmtV2')
ColubrisSSID,=mibBuilder.importSymbols('COLUBRIS-TC','ColubrisSSID')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
colubrisVscMIB=ModuleIdentity((1,3,6,1,4,1,8744,5,22))
_ColubrisVscMIBObjects_ObjectIdentity=ObjectIdentity
colubrisVscMIBObjects=_ColubrisVscMIBObjects_ObjectIdentity((1,3,6,1,4,1,8744,5,22,1))
_CoVscConfigGroup_ObjectIdentity=ObjectIdentity
coVscConfigGroup=_CoVscConfigGroup_ObjectIdentity((1,3,6,1,4,1,8744,5,22,1,1))
_CoVscConfigTable_Object=MibTable
coVscConfigTable=_CoVscConfigTable_Object((1,3,6,1,4,1,8744,5,22,1,1,1))
if mibBuilder.loadTexts:coVscConfigTable.setStatus(_A)
_CoVscConfigEntry_Object=MibTableRow
coVscConfigEntry=_CoVscConfigEntry_Object((1,3,6,1,4,1,8744,5,22,1,1,1,1))
coVscConfigEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:coVscConfigEntry.setStatus(_A)
class _CoVscCfgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CoVscCfgIndex_Type.__name__=_D
_CoVscCfgIndex_Object=MibTableColumn
coVscCfgIndex=_CoVscCfgIndex_Object((1,3,6,1,4,1,8744,5,22,1,1,1,1,1),_CoVscCfgIndex_Type())
coVscCfgIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:coVscCfgIndex.setStatus(_A)
_CoVscCfgFriendlyVscName_Type=DisplayString
_CoVscCfgFriendlyVscName_Object=MibTableColumn
coVscCfgFriendlyVscName=_CoVscCfgFriendlyVscName_Object((1,3,6,1,4,1,8744,5,22,1,1,1,1,2),_CoVscCfgFriendlyVscName_Type())
coVscCfgFriendlyVscName.setMaxAccess(_C)
if mibBuilder.loadTexts:coVscCfgFriendlyVscName.setStatus(_A)
_CoVscCfgSSID_Type=ColubrisSSID
_CoVscCfgSSID_Object=MibTableColumn
coVscCfgSSID=_CoVscCfgSSID_Object((1,3,6,1,4,1,8744,5,22,1,1,1,1,3),_CoVscCfgSSID_Type())
coVscCfgSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:coVscCfgSSID.setStatus(_A)
_CoVscCfgAccessControlled_Type=TruthValue
_CoVscCfgAccessControlled_Object=MibTableColumn
coVscCfgAccessControlled=_CoVscCfgAccessControlled_Object((1,3,6,1,4,1,8744,5,22,1,1,1,1,4),_CoVscCfgAccessControlled_Type())
coVscCfgAccessControlled.setMaxAccess(_C)
if mibBuilder.loadTexts:coVscCfgAccessControlled.setStatus(_A)
class _CoVscCfgSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('open',1),('ieee802dot1x',2),('wpa',3),('wpa2',4),('wpaAndWpa2',5)))
_CoVscCfgSecurity_Type.__name__=_D
_CoVscCfgSecurity_Object=MibTableColumn
coVscCfgSecurity=_CoVscCfgSecurity_Object((1,3,6,1,4,1,8744,5,22,1,1,1,1,5),_CoVscCfgSecurity_Type())
coVscCfgSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:coVscCfgSecurity.setStatus(_A)
class _CoVscCfgEncryption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('wep',2),('tkip',3),('aes',4),('tkipAndAes',5)))
_CoVscCfgEncryption_Type.__name__=_D
_CoVscCfgEncryption_Object=MibTableColumn
coVscCfgEncryption=_CoVscCfgEncryption_Object((1,3,6,1,4,1,8744,5,22,1,1,1,1,6),_CoVscCfgEncryption_Type())
coVscCfgEncryption.setMaxAccess(_C)
if mibBuilder.loadTexts:coVscCfgEncryption.setStatus(_A)
class _CoVscCfg8021xAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('radius',2),('psk',3)))
_CoVscCfg8021xAuthentication_Type.__name__=_D
_CoVscCfg8021xAuthentication_Object=MibTableColumn
coVscCfg8021xAuthentication=_CoVscCfg8021xAuthentication_Object((1,3,6,1,4,1,8744,5,22,1,1,1,1,7),_CoVscCfg8021xAuthentication_Type())
coVscCfg8021xAuthentication.setMaxAccess(_C)
if mibBuilder.loadTexts:coVscCfg8021xAuthentication.setStatus(_A)
_CoVscCfgMACAuthentication_Type=TruthValue
_CoVscCfgMACAuthentication_Object=MibTableColumn
coVscCfgMACAuthentication=_CoVscCfgMACAuthentication_Object((1,3,6,1,4,1,8744,5,22,1,1,1,1,8),_CoVscCfgMACAuthentication_Type())
coVscCfgMACAuthentication.setMaxAccess(_C)
if mibBuilder.loadTexts:coVscCfgMACAuthentication.setStatus(_A)
_CoVscCfgHTMLAuthentication_Type=TruthValue
_CoVscCfgHTMLAuthentication_Object=MibTableColumn
coVscCfgHTMLAuthentication=_CoVscCfgHTMLAuthentication_Object((1,3,6,1,4,1,8744,5,22,1,1,1,1,9),_CoVscCfgHTMLAuthentication_Type())
coVscCfgHTMLAuthentication.setMaxAccess(_C)
if mibBuilder.loadTexts:coVscCfgHTMLAuthentication.setStatus(_A)
_ColubrisVscMIBConformance_ObjectIdentity=ObjectIdentity
colubrisVscMIBConformance=_ColubrisVscMIBConformance_ObjectIdentity((1,3,6,1,4,1,8744,5,22,2))
_ColubrisVscMIBCompliances_ObjectIdentity=ObjectIdentity
colubrisVscMIBCompliances=_ColubrisVscMIBCompliances_ObjectIdentity((1,3,6,1,4,1,8744,5,22,2,1))
_ColubrisVscMIBGroups_ObjectIdentity=ObjectIdentity
colubrisVscMIBGroups=_ColubrisVscMIBGroups_ObjectIdentity((1,3,6,1,4,1,8744,5,22,2,2))
colubrisVscMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,22,2,2,1))
colubrisVscMIBGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:colubrisVscMIBGroup.setStatus(_A)
colubrisVscMIBCompliance=ModuleCompliance((1,3,6,1,4,1,8744,5,22,2,1,1))
colubrisVscMIBCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:colubrisVscMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'colubrisVscMIB':colubrisVscMIB,'colubrisVscMIBObjects':colubrisVscMIBObjects,'coVscConfigGroup':coVscConfigGroup,'coVscConfigTable':coVscConfigTable,'coVscConfigEntry':coVscConfigEntry,_E:coVscCfgIndex,_F:coVscCfgFriendlyVscName,_G:coVscCfgSSID,_H:coVscCfgAccessControlled,_I:coVscCfgSecurity,_J:coVscCfgEncryption,_K:coVscCfg8021xAuthentication,_L:coVscCfgMACAuthentication,_M:coVscCfgHTMLAuthentication,'colubrisVscMIBConformance':colubrisVscMIBConformance,'colubrisVscMIBCompliances':colubrisVscMIBCompliances,'colubrisVscMIBCompliance':colubrisVscMIBCompliance,'colubrisVscMIBGroups':colubrisVscMIBGroups,_N:colubrisVscMIBGroup})