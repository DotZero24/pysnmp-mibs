_K='ciscoIfLoopbackGroup'
_J='cifLRowStatus'
_I='cifLFELoopbackDeviceAndCode'
_H='cifLLoopbackStatus'
_G='cifLLoopback'
_F='ifIndex'
_E='IF-MIB'
_D='read-create'
_C='Integer32'
_B='CISCO-IF-LOOPBACK-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoIfLoopbackMIB=ModuleIdentity((1,3,6,1,4,1,9,9,9399))
if mibBuilder.loadTexts:ciscoIfLoopbackMIB.setRevisions(('2001-11-15 00:00',))
_CiscoIfLoopbackMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIfLoopbackMIBObjects=_CiscoIfLoopbackMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,9399,1))
_CiscoIfLoopbackConfig_ObjectIdentity=ObjectIdentity
ciscoIfLoopbackConfig=_CiscoIfLoopbackConfig_ObjectIdentity((1,3,6,1,4,1,9,9,9399,1,1))
_CifLConfTable_Object=MibTable
cifLConfTable=_CifLConfTable_Object((1,3,6,1,4,1,9,9,9399,1,1,1))
if mibBuilder.loadTexts:cifLConfTable.setStatus(_A)
_CifLConfEntry_Object=MibTableRow
cifLConfEntry=_CifLConfEntry_Object((1,3,6,1,4,1,9,9,9399,1,1,1,1))
cifLConfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cifLConfEntry.setStatus(_A)
class _CifLLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('farEndLineLoopback',1),('farEndPayloadLoopback',2),('remoteLineLoopback',3),('remotePayloadLoopback',4),('localLoopback',5)))
_CifLLoopback_Type.__name__=_C
_CifLLoopback_Object=MibTableColumn
cifLLoopback=_CifLLoopback_Object((1,3,6,1,4,1,9,9,9399,1,1,1,1,1),_CifLLoopback_Type())
cifLLoopback.setMaxAccess(_D)
if mibBuilder.loadTexts:cifLLoopback.setStatus(_A)
class _CifLLoopbackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('completed',1),('inProgress',2),('clockOutOfSync',3),('failed',4)))
_CifLLoopbackStatus_Type.__name__=_C
_CifLLoopbackStatus_Object=MibTableColumn
cifLLoopbackStatus=_CifLLoopbackStatus_Object((1,3,6,1,4,1,9,9,9399,1,1,1,1,2),_CifLLoopbackStatus_Type())
cifLLoopbackStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:cifLLoopbackStatus.setStatus(_A)
class _CifLFELoopbackDeviceAndCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('nonLatchOCUwith1',1),('nonLatchOCUwithout1',2),('nonLatchCSU',3),('nonLatchDSU',4),('latchDS0Drop',5),('latchDS0Line',6),('latchOCU',7),('latchCSU',8),('latchDSU',9),('latchHL96',10),('v54PN127Polynomial',11),('lineInband',12),('lineLoopbackESF',13),('payloadLoopbackESF',14),('noCode',15),('lineLoopbackFEAC',16),('smartJackInband',17)))
_CifLFELoopbackDeviceAndCode_Type.__name__=_C
_CifLFELoopbackDeviceAndCode_Object=MibTableColumn
cifLFELoopbackDeviceAndCode=_CifLFELoopbackDeviceAndCode_Object((1,3,6,1,4,1,9,9,9399,1,1,1,1,3),_CifLFELoopbackDeviceAndCode_Type())
cifLFELoopbackDeviceAndCode.setMaxAccess(_D)
if mibBuilder.loadTexts:cifLFELoopbackDeviceAndCode.setStatus(_A)
_CifLRowStatus_Type=RowStatus
_CifLRowStatus_Object=MibTableColumn
cifLRowStatus=_CifLRowStatus_Object((1,3,6,1,4,1,9,9,9399,1,1,1,1,4),_CifLRowStatus_Type())
cifLRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cifLRowStatus.setStatus(_A)
_CiscoIfLoopbackMIBConformance_ObjectIdentity=ObjectIdentity
ciscoIfLoopbackMIBConformance=_CiscoIfLoopbackMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,9399,8))
_CiscoIfLoopbackMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIfLoopbackMIBCompliances=_CiscoIfLoopbackMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,9399,8,1))
_CiscoIfLoopbackMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIfLoopbackMIBGroups=_CiscoIfLoopbackMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,9399,8,2))
ciscoIfLoopbackGroup=ObjectGroup((1,3,6,1,4,1,9,9,9399,8,2,1))
ciscoIfLoopbackGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:ciscoIfLoopbackGroup.setStatus(_A)
ciscoIfLoopbackMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,9399,8,1,1))
ciscoIfLoopbackMIBCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:ciscoIfLoopbackMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIfLoopbackMIB':ciscoIfLoopbackMIB,'ciscoIfLoopbackMIBObjects':ciscoIfLoopbackMIBObjects,'ciscoIfLoopbackConfig':ciscoIfLoopbackConfig,'cifLConfTable':cifLConfTable,'cifLConfEntry':cifLConfEntry,_G:cifLLoopback,_H:cifLLoopbackStatus,_I:cifLFELoopbackDeviceAndCode,_J:cifLRowStatus,'ciscoIfLoopbackMIBConformance':ciscoIfLoopbackMIBConformance,'ciscoIfLoopbackMIBCompliances':ciscoIfLoopbackMIBCompliances,'ciscoIfLoopbackMIBCompliance':ciscoIfLoopbackMIBCompliance,'ciscoIfLoopbackMIBGroups':ciscoIfLoopbackMIBGroups,_K:ciscoIfLoopbackGroup})