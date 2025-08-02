_K='eltULDLinkStatus'
_J='ELTEX-MES-ULD-MIB'
_I='read-only'
_H='disabled'
_G='enabled'
_F='TruthValue'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='Integer32'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesMng,=mibBuilder.importSymbols('ELTEX-MES','eltMesMng')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
eltMesULDMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,23,1,87))
if mibBuilder.loadTexts:eltMesULDMIB.setRevisions(('2015-11-19 00:00',))
_EltMesULDNotifications_ObjectIdentity=ObjectIdentity
eltMesULDNotifications=_EltMesULDNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,87,0))
_EltMesULDMgmt_ObjectIdentity=ObjectIdentity
eltMesULDMgmt=_EltMesULDMgmt_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,87,1))
_EltULDTable_Object=MibTable
eltULDTable=_EltULDTable_Object((1,3,6,1,4,1,35265,1,23,1,87,1,1))
if mibBuilder.loadTexts:eltULDTable.setStatus(_A)
_EltULDEntry_Object=MibTableRow
eltULDEntry=_EltULDEntry_Object((1,3,6,1,4,1,35265,1,23,1,87,1,1,1))
eltULDEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:eltULDEntry.setStatus(_A)
class _EltULDAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_EltULDAdminState_Type.__name__=_B
_EltULDAdminState_Object=MibTableColumn
eltULDAdminState=_EltULDAdminState_Object((1,3,6,1,4,1,35265,1,23,1,87,1,1,1,1),_EltULDAdminState_Type())
eltULDAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:eltULDAdminState.setStatus(_A)
class _EltULDOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_EltULDOperStatus_Type.__name__=_B
_EltULDOperStatus_Object=MibTableColumn
eltULDOperStatus=_EltULDOperStatus_Object((1,3,6,1,4,1,35265,1,23,1,87,1,1,1,2),_EltULDOperStatus_Type())
eltULDOperStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:eltULDOperStatus.setStatus(_A)
class _EltULDMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('log',1),('err-disable',2)))
_EltULDMode_Type.__name__=_B
_EltULDMode_Object=MibTableColumn
eltULDMode=_EltULDMode_Object((1,3,6,1,4,1,35265,1,23,1,87,1,1,1,3),_EltULDMode_Type())
eltULDMode.setMaxAccess(_C)
if mibBuilder.loadTexts:eltULDMode.setStatus(_A)
class _EltULDDiscoveryTime_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,300))
_EltULDDiscoveryTime_Type.__name__=_B
_EltULDDiscoveryTime_Object=MibTableColumn
eltULDDiscoveryTime=_EltULDDiscoveryTime_Object((1,3,6,1,4,1,35265,1,23,1,87,1,1,1,4),_EltULDDiscoveryTime_Type())
eltULDDiscoveryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:eltULDDiscoveryTime.setStatus(_A)
class _EltULDIsAggressive_Type(TruthValue):defaultValue=2
_EltULDIsAggressive_Type.__name__=_F
_EltULDIsAggressive_Object=MibTableColumn
eltULDIsAggressive=_EltULDIsAggressive_Object((1,3,6,1,4,1,35265,1,23,1,87,1,1,1,5),_EltULDIsAggressive_Type())
eltULDIsAggressive.setMaxAccess(_C)
if mibBuilder.loadTexts:eltULDIsAggressive.setStatus(_A)
class _EltULDLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('unidirectional',2),('bidirectional',3),('tx-rx-loop',4),('neighbor-mismatch',5)))
_EltULDLinkStatus_Type.__name__=_B
_EltULDLinkStatus_Object=MibTableColumn
eltULDLinkStatus=_EltULDLinkStatus_Object((1,3,6,1,4,1,35265,1,23,1,87,1,1,1,6),_EltULDLinkStatus_Type())
eltULDLinkStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:eltULDLinkStatus.setStatus(_A)
eltULDLinkStatusChanged=NotificationType((1,3,6,1,4,1,35265,1,23,1,87,0,1))
eltULDLinkStatusChanged.setObjects(*((_D,_E),(_J,_K)))
if mibBuilder.loadTexts:eltULDLinkStatusChanged.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'eltMesULDMIB':eltMesULDMIB,'eltMesULDNotifications':eltMesULDNotifications,'eltULDLinkStatusChanged':eltULDLinkStatusChanged,'eltMesULDMgmt':eltMesULDMgmt,'eltULDTable':eltULDTable,'eltULDEntry':eltULDEntry,'eltULDAdminState':eltULDAdminState,'eltULDOperStatus':eltULDOperStatus,'eltULDMode':eltULDMode,'eltULDDiscoveryTime':eltULDDiscoveryTime,'eltULDIsAggressive':eltULDIsAggressive,_K:eltULDLinkStatus})