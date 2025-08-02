_R='dpLldpExtBasicCfgGroup'
_Q='dpLldpExtLldpTrapEnabled'
_P='dpLldpExtLldpEnabled'
_O='interfaceName'
_N='networkAddress'
_M='macAddress'
_L='portComponent'
_K='interfaceAlias'
_J='not-accessible'
_I='dpLldpExtRemIndex'
_H='dpLldpExtRemLocalPortNum'
_G='read-write'
_F='SnmpAdminString'
_E='OctetString'
_D='read-only'
_C='Integer32'
_B='DLINKPRIME-LLDP-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
dlinkPrimeLldpExtMIB=ModuleIdentity((1,3,6,1,4,1,171,15,8))
if mibBuilder.loadTexts:dlinkPrimeLldpExtMIB.setRevisions(('2014-06-03 00:00',))
_DpLldpExtMIBNotifications_ObjectIdentity=ObjectIdentity
dpLldpExtMIBNotifications=_DpLldpExtMIBNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,8,0))
_DpLldpExtMIBObjects_ObjectIdentity=ObjectIdentity
dpLldpExtMIBObjects=_DpLldpExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,8,1))
_DpLldpExtLldpEnabled_Type=TruthValue
_DpLldpExtLldpEnabled_Object=MibScalar
dpLldpExtLldpEnabled=_DpLldpExtLldpEnabled_Object((1,3,6,1,4,1,171,15,8,1,1),_DpLldpExtLldpEnabled_Type())
dpLldpExtLldpEnabled.setMaxAccess(_G)
if mibBuilder.loadTexts:dpLldpExtLldpEnabled.setStatus(_A)
_DpLldpExtLldpTrapEnabled_Type=TruthValue
_DpLldpExtLldpTrapEnabled_Object=MibScalar
dpLldpExtLldpTrapEnabled=_DpLldpExtLldpTrapEnabled_Object((1,3,6,1,4,1,171,15,8,1,2),_DpLldpExtLldpTrapEnabled_Type())
dpLldpExtLldpTrapEnabled.setMaxAccess(_G)
if mibBuilder.loadTexts:dpLldpExtLldpTrapEnabled.setStatus(_A)
_DpLldpExtRemTable_Object=MibTable
dpLldpExtRemTable=_DpLldpExtRemTable_Object((1,3,6,1,4,1,171,15,8,1,3))
if mibBuilder.loadTexts:dpLldpExtRemTable.setStatus(_A)
_DpLldpExtRemEntry_Object=MibTableRow
dpLldpExtRemEntry=_DpLldpExtRemEntry_Object((1,3,6,1,4,1,171,15,8,1,3,1))
dpLldpExtRemEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:dpLldpExtRemEntry.setStatus(_A)
class _DpLldpExtRemLocalPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_DpLldpExtRemLocalPortNum_Type.__name__=_C
_DpLldpExtRemLocalPortNum_Object=MibTableColumn
dpLldpExtRemLocalPortNum=_DpLldpExtRemLocalPortNum_Object((1,3,6,1,4,1,171,15,8,1,3,1,1),_DpLldpExtRemLocalPortNum_Type())
dpLldpExtRemLocalPortNum.setMaxAccess(_J)
if mibBuilder.loadTexts:dpLldpExtRemLocalPortNum.setStatus(_A)
class _DpLldpExtRemIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DpLldpExtRemIndex_Type.__name__=_C
_DpLldpExtRemIndex_Object=MibTableColumn
dpLldpExtRemIndex=_DpLldpExtRemIndex_Object((1,3,6,1,4,1,171,15,8,1,3,1,2),_DpLldpExtRemIndex_Type())
dpLldpExtRemIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:dpLldpExtRemIndex.setStatus(_A)
class _DpLldpExtRemChassisIdSubtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('chassisComponent',1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),('local',7)))
_DpLldpExtRemChassisIdSubtype_Type.__name__=_C
_DpLldpExtRemChassisIdSubtype_Object=MibTableColumn
dpLldpExtRemChassisIdSubtype=_DpLldpExtRemChassisIdSubtype_Object((1,3,6,1,4,1,171,15,8,1,3,1,3),_DpLldpExtRemChassisIdSubtype_Type())
dpLldpExtRemChassisIdSubtype.setMaxAccess(_D)
if mibBuilder.loadTexts:dpLldpExtRemChassisIdSubtype.setStatus(_A)
class _DpLldpExtRemChassisId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_DpLldpExtRemChassisId_Type.__name__=_E
_DpLldpExtRemChassisId_Object=MibTableColumn
dpLldpExtRemChassisId=_DpLldpExtRemChassisId_Object((1,3,6,1,4,1,171,15,8,1,3,1,4),_DpLldpExtRemChassisId_Type())
dpLldpExtRemChassisId.setMaxAccess(_D)
if mibBuilder.loadTexts:dpLldpExtRemChassisId.setStatus(_A)
class _DpLldpExtRemPortIdSubtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4),(_O,5),('agentCircuitId',6),('local',7)))
_DpLldpExtRemPortIdSubtype_Type.__name__=_C
_DpLldpExtRemPortIdSubtype_Object=MibTableColumn
dpLldpExtRemPortIdSubtype=_DpLldpExtRemPortIdSubtype_Object((1,3,6,1,4,1,171,15,8,1,3,1,5),_DpLldpExtRemPortIdSubtype_Type())
dpLldpExtRemPortIdSubtype.setMaxAccess(_D)
if mibBuilder.loadTexts:dpLldpExtRemPortIdSubtype.setStatus(_A)
class _DpLldpExtRemPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_DpLldpExtRemPortId_Type.__name__=_E
_DpLldpExtRemPortId_Object=MibTableColumn
dpLldpExtRemPortId=_DpLldpExtRemPortId_Object((1,3,6,1,4,1,171,15,8,1,3,1,6),_DpLldpExtRemPortId_Type())
dpLldpExtRemPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:dpLldpExtRemPortId.setStatus(_A)
class _DpLldpExtRemPortDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DpLldpExtRemPortDesc_Type.__name__=_F
_DpLldpExtRemPortDesc_Object=MibTableColumn
dpLldpExtRemPortDesc=_DpLldpExtRemPortDesc_Object((1,3,6,1,4,1,171,15,8,1,3,1,7),_DpLldpExtRemPortDesc_Type())
dpLldpExtRemPortDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:dpLldpExtRemPortDesc.setStatus(_A)
_DpLldpExtMIBConformance_ObjectIdentity=ObjectIdentity
dpLldpExtMIBConformance=_DpLldpExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,8,2))
_DpLldpExtMIBCompliances_ObjectIdentity=ObjectIdentity
dpLldpExtMIBCompliances=_DpLldpExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,8,2,1))
_DpLldpExtMIBGroups_ObjectIdentity=ObjectIdentity
dpLldpExtMIBGroups=_DpLldpExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,15,8,2,2))
dpLldpExtBasicCfgGroup=ObjectGroup((1,3,6,1,4,1,171,15,8,2,2,1))
dpLldpExtBasicCfgGroup.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:dpLldpExtBasicCfgGroup.setStatus(_A)
dpLldpExtDatabaseChanged=NotificationType((1,3,6,1,4,1,171,15,8,0,1))
if mibBuilder.loadTexts:dpLldpExtDatabaseChanged.setStatus(_A)
dpLldpExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,8,2,1,1))
dpLldpExtMIBCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:dpLldpExtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlinkPrimeLldpExtMIB':dlinkPrimeLldpExtMIB,'dpLldpExtMIBNotifications':dpLldpExtMIBNotifications,'dpLldpExtDatabaseChanged':dpLldpExtDatabaseChanged,'dpLldpExtMIBObjects':dpLldpExtMIBObjects,_P:dpLldpExtLldpEnabled,_Q:dpLldpExtLldpTrapEnabled,'dpLldpExtRemTable':dpLldpExtRemTable,'dpLldpExtRemEntry':dpLldpExtRemEntry,_H:dpLldpExtRemLocalPortNum,_I:dpLldpExtRemIndex,'dpLldpExtRemChassisIdSubtype':dpLldpExtRemChassisIdSubtype,'dpLldpExtRemChassisId':dpLldpExtRemChassisId,'dpLldpExtRemPortIdSubtype':dpLldpExtRemPortIdSubtype,'dpLldpExtRemPortId':dpLldpExtRemPortId,'dpLldpExtRemPortDesc':dpLldpExtRemPortDesc,'dpLldpExtMIBConformance':dpLldpExtMIBConformance,'dpLldpExtMIBCompliances':dpLldpExtMIBCompliances,'dpLldpExtMIBCompliance':dpLldpExtMIBCompliance,'dpLldpExtMIBGroups':dpLldpExtMIBGroups,_R:dpLldpExtBasicCfgGroup})