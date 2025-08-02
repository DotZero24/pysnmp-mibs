_N='ipSecPhaseTwoPolMapGroup'
_M='ipSecPhaseOnePolMapGroup'
_L='ipSecPolMapAceString'
_K='ipSecPolMapAclString'
_J='ipSecPolMapCryptoMapNum'
_I='ipSecPolMapCryptoMapName'
_H='ikePolMapPolicyNum'
_G='ipSecPolMapTunIndex'
_F='not-accessible'
_E='ikePolMapTunIndex'
_D='read-only'
_C='Integer32'
_B='CISCO-IPSEC-POLICY-MAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoIpSecPolMapMIB=ModuleIdentity((1,3,6,1,4,1,9,9,172))
_CiscoIpSecPolMapMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIpSecPolMapMIBObjects=_CiscoIpSecPolMapMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,172,1))
_IpSecPhaseOnePolMap_ObjectIdentity=ObjectIdentity
ipSecPhaseOnePolMap=_IpSecPhaseOnePolMap_ObjectIdentity((1,3,6,1,4,1,9,9,172,1,1))
_IkePolMapTable_Object=MibTable
ikePolMapTable=_IkePolMapTable_Object((1,3,6,1,4,1,9,9,172,1,1,1))
if mibBuilder.loadTexts:ikePolMapTable.setStatus(_A)
_IkePolMapEntry_Object=MibTableRow
ikePolMapEntry=_IkePolMapEntry_Object((1,3,6,1,4,1,9,9,172,1,1,1,1))
ikePolMapEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:ikePolMapEntry.setStatus(_A)
class _IkePolMapTunIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IkePolMapTunIndex_Type.__name__=_C
_IkePolMapTunIndex_Object=MibTableColumn
ikePolMapTunIndex=_IkePolMapTunIndex_Object((1,3,6,1,4,1,9,9,172,1,1,1,1,1),_IkePolMapTunIndex_Type())
ikePolMapTunIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ikePolMapTunIndex.setStatus(_A)
class _IkePolMapPolicyNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IkePolMapPolicyNum_Type.__name__=_C
_IkePolMapPolicyNum_Object=MibTableColumn
ikePolMapPolicyNum=_IkePolMapPolicyNum_Object((1,3,6,1,4,1,9,9,172,1,1,1,1,2),_IkePolMapPolicyNum_Type())
ikePolMapPolicyNum.setMaxAccess(_D)
if mibBuilder.loadTexts:ikePolMapPolicyNum.setStatus(_A)
_IpSecPhaseTwoPolMap_ObjectIdentity=ObjectIdentity
ipSecPhaseTwoPolMap=_IpSecPhaseTwoPolMap_ObjectIdentity((1,3,6,1,4,1,9,9,172,1,2))
_IpSecPolMapTable_Object=MibTable
ipSecPolMapTable=_IpSecPolMapTable_Object((1,3,6,1,4,1,9,9,172,1,2,1))
if mibBuilder.loadTexts:ipSecPolMapTable.setStatus(_A)
_IpSecPolMapEntry_Object=MibTableRow
ipSecPolMapEntry=_IpSecPolMapEntry_Object((1,3,6,1,4,1,9,9,172,1,2,1,1))
ipSecPolMapEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:ipSecPolMapEntry.setStatus(_A)
class _IpSecPolMapTunIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IpSecPolMapTunIndex_Type.__name__=_C
_IpSecPolMapTunIndex_Object=MibTableColumn
ipSecPolMapTunIndex=_IpSecPolMapTunIndex_Object((1,3,6,1,4,1,9,9,172,1,2,1,1,1),_IpSecPolMapTunIndex_Type())
ipSecPolMapTunIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ipSecPolMapTunIndex.setStatus(_A)
_IpSecPolMapCryptoMapName_Type=DisplayString
_IpSecPolMapCryptoMapName_Object=MibTableColumn
ipSecPolMapCryptoMapName=_IpSecPolMapCryptoMapName_Object((1,3,6,1,4,1,9,9,172,1,2,1,1,2),_IpSecPolMapCryptoMapName_Type())
ipSecPolMapCryptoMapName.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSecPolMapCryptoMapName.setStatus(_A)
class _IpSecPolMapCryptoMapNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IpSecPolMapCryptoMapNum_Type.__name__=_C
_IpSecPolMapCryptoMapNum_Object=MibTableColumn
ipSecPolMapCryptoMapNum=_IpSecPolMapCryptoMapNum_Object((1,3,6,1,4,1,9,9,172,1,2,1,1,3),_IpSecPolMapCryptoMapNum_Type())
ipSecPolMapCryptoMapNum.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSecPolMapCryptoMapNum.setStatus(_A)
_IpSecPolMapAclString_Type=DisplayString
_IpSecPolMapAclString_Object=MibTableColumn
ipSecPolMapAclString=_IpSecPolMapAclString_Object((1,3,6,1,4,1,9,9,172,1,2,1,1,4),_IpSecPolMapAclString_Type())
ipSecPolMapAclString.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSecPolMapAclString.setStatus(_A)
_IpSecPolMapAceString_Type=DisplayString
_IpSecPolMapAceString_Object=MibTableColumn
ipSecPolMapAceString=_IpSecPolMapAceString_Object((1,3,6,1,4,1,9,9,172,1,2,1,1,5),_IpSecPolMapAceString_Type())
ipSecPolMapAceString.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSecPolMapAceString.setStatus(_A)
_CiscoIpSecPolMapMIBNotifPrefix_ObjectIdentity=ObjectIdentity
ciscoIpSecPolMapMIBNotifPrefix=_CiscoIpSecPolMapMIBNotifPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,172,2))
_CiscoIpSecPolMapMIBConformance_ObjectIdentity=ObjectIdentity
ciscoIpSecPolMapMIBConformance=_CiscoIpSecPolMapMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,172,3))
_IpSecPolMapMIBGroups_ObjectIdentity=ObjectIdentity
ipSecPolMapMIBGroups=_IpSecPolMapMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,172,3,1))
_IpSecPolMapMIBCompliances_ObjectIdentity=ObjectIdentity
ipSecPolMapMIBCompliances=_IpSecPolMapMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,172,3,2))
ipSecPhaseOnePolMapGroup=ObjectGroup((1,3,6,1,4,1,9,9,172,3,1,1))
ipSecPhaseOnePolMapGroup.setObjects((_B,_H))
if mibBuilder.loadTexts:ipSecPhaseOnePolMapGroup.setStatus(_A)
ipSecPhaseTwoPolMapGroup=ObjectGroup((1,3,6,1,4,1,9,9,172,3,1,2))
ipSecPhaseTwoPolMapGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:ipSecPhaseTwoPolMapGroup.setStatus(_A)
ipSecPolMapMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,172,3,2,1))
ipSecPolMapMIBCompliance.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ipSecPolMapMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIpSecPolMapMIB':ciscoIpSecPolMapMIB,'ciscoIpSecPolMapMIBObjects':ciscoIpSecPolMapMIBObjects,'ipSecPhaseOnePolMap':ipSecPhaseOnePolMap,'ikePolMapTable':ikePolMapTable,'ikePolMapEntry':ikePolMapEntry,_E:ikePolMapTunIndex,_H:ikePolMapPolicyNum,'ipSecPhaseTwoPolMap':ipSecPhaseTwoPolMap,'ipSecPolMapTable':ipSecPolMapTable,'ipSecPolMapEntry':ipSecPolMapEntry,_G:ipSecPolMapTunIndex,_I:ipSecPolMapCryptoMapName,_J:ipSecPolMapCryptoMapNum,_K:ipSecPolMapAclString,_L:ipSecPolMapAceString,'ciscoIpSecPolMapMIBNotifPrefix':ciscoIpSecPolMapMIBNotifPrefix,'ciscoIpSecPolMapMIBConformance':ciscoIpSecPolMapMIBConformance,'ipSecPolMapMIBGroups':ipSecPolMapMIBGroups,_M:ipSecPhaseOnePolMapGroup,_N:ipSecPhaseTwoPolMapGroup,'ipSecPolMapMIBCompliances':ipSecPolMapMIBCompliances,'ipSecPolMapMIBCompliance':ipSecPolMapMIBCompliance})