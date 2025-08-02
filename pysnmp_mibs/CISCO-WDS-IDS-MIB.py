_O='ciscoWdsIdsMacSpoofingGroup'
_N='ciscoWdsIdsMacSpoofDetectTime'
_M='ciscoWdsIdsMacSpoofUserId'
_L='ciscoWdsIdsMacSpoofClient'
_K='ciscoWdsIdsMaxEntriesPerMac'
_J='ciscoWdsIdsMaxMacAddresses'
_I='not-accessible'
_H='ciscoWdsIdsMacSpoofIndex'
_G='ciscoWdsIdsMacSpoofStaMacAddress'
_F='read-write'
_E='SnmpAdminString'
_D='read-only'
_C='Integer32'
_B='CISCO-WDS-IDS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeStamp')
ciscoWdsIdsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,457))
if mibBuilder.loadTexts:ciscoWdsIdsMIB.setRevisions(('2004-10-17 00:00',))
_CiscoWdsIdsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWdsIdsMIBObjects=_CiscoWdsIdsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,457,1))
_CiscoWdsIdsMacSpoofing_ObjectIdentity=ObjectIdentity
ciscoWdsIdsMacSpoofing=_CiscoWdsIdsMacSpoofing_ObjectIdentity((1,3,6,1,4,1,9,9,457,1,1))
class _CiscoWdsIdsMaxMacAddresses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CiscoWdsIdsMaxMacAddresses_Type.__name__=_C
_CiscoWdsIdsMaxMacAddresses_Object=MibScalar
ciscoWdsIdsMaxMacAddresses=_CiscoWdsIdsMaxMacAddresses_Object((1,3,6,1,4,1,9,9,457,1,1,1),_CiscoWdsIdsMaxMacAddresses_Type())
ciscoWdsIdsMaxMacAddresses.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoWdsIdsMaxMacAddresses.setStatus(_A)
class _CiscoWdsIdsMaxEntriesPerMac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CiscoWdsIdsMaxEntriesPerMac_Type.__name__=_C
_CiscoWdsIdsMaxEntriesPerMac_Object=MibScalar
ciscoWdsIdsMaxEntriesPerMac=_CiscoWdsIdsMaxEntriesPerMac_Object((1,3,6,1,4,1,9,9,457,1,1,2),_CiscoWdsIdsMaxEntriesPerMac_Type())
ciscoWdsIdsMaxEntriesPerMac.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoWdsIdsMaxEntriesPerMac.setStatus(_A)
_CiscoWdsIdsMacSpoofTable_Object=MibTable
ciscoWdsIdsMacSpoofTable=_CiscoWdsIdsMacSpoofTable_Object((1,3,6,1,4,1,9,9,457,1,1,3))
if mibBuilder.loadTexts:ciscoWdsIdsMacSpoofTable.setStatus(_A)
_CiscoWdsIdsMacSpoofEntry_Object=MibTableRow
ciscoWdsIdsMacSpoofEntry=_CiscoWdsIdsMacSpoofEntry_Object((1,3,6,1,4,1,9,9,457,1,1,3,1))
ciscoWdsIdsMacSpoofEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:ciscoWdsIdsMacSpoofEntry.setStatus(_A)
_CiscoWdsIdsMacSpoofStaMacAddress_Type=MacAddress
_CiscoWdsIdsMacSpoofStaMacAddress_Object=MibTableColumn
ciscoWdsIdsMacSpoofStaMacAddress=_CiscoWdsIdsMacSpoofStaMacAddress_Object((1,3,6,1,4,1,9,9,457,1,1,3,1,1),_CiscoWdsIdsMacSpoofStaMacAddress_Type())
ciscoWdsIdsMacSpoofStaMacAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:ciscoWdsIdsMacSpoofStaMacAddress.setStatus(_A)
_CiscoWdsIdsMacSpoofIndex_Type=Unsigned32
_CiscoWdsIdsMacSpoofIndex_Object=MibTableColumn
ciscoWdsIdsMacSpoofIndex=_CiscoWdsIdsMacSpoofIndex_Object((1,3,6,1,4,1,9,9,457,1,1,3,1,2),_CiscoWdsIdsMacSpoofIndex_Type())
ciscoWdsIdsMacSpoofIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ciscoWdsIdsMacSpoofIndex.setStatus(_A)
_CiscoWdsIdsMacSpoofClient_Type=MacAddress
_CiscoWdsIdsMacSpoofClient_Object=MibTableColumn
ciscoWdsIdsMacSpoofClient=_CiscoWdsIdsMacSpoofClient_Object((1,3,6,1,4,1,9,9,457,1,1,3,1,3),_CiscoWdsIdsMacSpoofClient_Type())
ciscoWdsIdsMacSpoofClient.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoWdsIdsMacSpoofClient.setStatus(_A)
class _CiscoWdsIdsMacSpoofUserId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,253))
_CiscoWdsIdsMacSpoofUserId_Type.__name__=_E
_CiscoWdsIdsMacSpoofUserId_Object=MibTableColumn
ciscoWdsIdsMacSpoofUserId=_CiscoWdsIdsMacSpoofUserId_Object((1,3,6,1,4,1,9,9,457,1,1,3,1,4),_CiscoWdsIdsMacSpoofUserId_Type())
ciscoWdsIdsMacSpoofUserId.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoWdsIdsMacSpoofUserId.setStatus(_A)
_CiscoWdsIdsMacSpoofDetectTime_Type=TimeStamp
_CiscoWdsIdsMacSpoofDetectTime_Object=MibTableColumn
ciscoWdsIdsMacSpoofDetectTime=_CiscoWdsIdsMacSpoofDetectTime_Object((1,3,6,1,4,1,9,9,457,1,1,3,1,5),_CiscoWdsIdsMacSpoofDetectTime_Type())
ciscoWdsIdsMacSpoofDetectTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoWdsIdsMacSpoofDetectTime.setStatus(_A)
_CiscoWdsIdsMIBConform_ObjectIdentity=ObjectIdentity
ciscoWdsIdsMIBConform=_CiscoWdsIdsMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,457,2))
_CiscoWdsIdsMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWdsIdsMIBCompliances=_CiscoWdsIdsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,457,2,1))
_CiscoWdsIdsMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWdsIdsMIBGroups=_CiscoWdsIdsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,457,2,2))
ciscoWdsIdsMacSpoofingGroup=ObjectGroup((1,3,6,1,4,1,9,9,457,2,2,1))
ciscoWdsIdsMacSpoofingGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ciscoWdsIdsMacSpoofingGroup.setStatus(_A)
ciscoWdsIdsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,457,2,1,1))
ciscoWdsIdsMIBCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:ciscoWdsIdsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoWdsIdsMIB':ciscoWdsIdsMIB,'ciscoWdsIdsMIBObjects':ciscoWdsIdsMIBObjects,'ciscoWdsIdsMacSpoofing':ciscoWdsIdsMacSpoofing,_J:ciscoWdsIdsMaxMacAddresses,_K:ciscoWdsIdsMaxEntriesPerMac,'ciscoWdsIdsMacSpoofTable':ciscoWdsIdsMacSpoofTable,'ciscoWdsIdsMacSpoofEntry':ciscoWdsIdsMacSpoofEntry,_G:ciscoWdsIdsMacSpoofStaMacAddress,_H:ciscoWdsIdsMacSpoofIndex,_L:ciscoWdsIdsMacSpoofClient,_M:ciscoWdsIdsMacSpoofUserId,_N:ciscoWdsIdsMacSpoofDetectTime,'ciscoWdsIdsMIBConform':ciscoWdsIdsMIBConform,'ciscoWdsIdsMIBCompliances':ciscoWdsIdsMIBCompliances,'ciscoWdsIdsMIBCompliance':ciscoWdsIdsMIBCompliance,'ciscoWdsIdsMIBGroups':ciscoWdsIdsMIBGroups,_O:ciscoWdsIdsMacSpoofingGroup})