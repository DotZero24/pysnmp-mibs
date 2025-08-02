_P='osL2PduGuardMandatoryGroup'
_O='osL2PduGuardState'
_N='osL2PduGuardInformRate'
_M='osL2PduGuardIsolateRate'
_L='osL2PduGuardSupprt'
_K='packets per second'
_J='read-write'
_I='not-accessible'
_H='osL2PduGuardPort'
_G='osL2PduGuardProtocol'
_F='read-only'
_E='unknown'
_D='Integer32'
_C='Unsigned32'
_B='OS-L2-PDU-GUARD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
oaOptiSwitch,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','oaOptiSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
osL2PduGuard=ModuleIdentity((1,3,6,1,4,1,6926,2,17))
if mibBuilder.loadTexts:osL2PduGuard.setRevisions(('2010-01-09 00:00',))
class L2ProtocolId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*((_E,1),('stp',2),('ethoam',3),('efm',4),('dot1x',5),('esmc',6),('cdp',7),('dtp',8),('udld',9),('pagp',10),('pvst',11),('vtp',12),('lacp',13),('erp',14),('lamp',15),('elmi',16),('lldp',17),('garp',18)))
class L2PortState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('normal',2),('isolated',3),('inform',4)))
class SupportValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSupported',1),('supported',2)))
_OsL2PduGuardCpGen_ObjectIdentity=ObjectIdentity
osL2PduGuardCpGen=_OsL2PduGuardCpGen_ObjectIdentity((1,3,6,1,4,1,6926,2,17,1))
_OsL2PduGuardSupprt_Type=SupportValue
_OsL2PduGuardSupprt_Object=MibScalar
osL2PduGuardSupprt=_OsL2PduGuardSupprt_Object((1,3,6,1,4,1,6926,2,17,1,1),_OsL2PduGuardSupprt_Type())
osL2PduGuardSupprt.setMaxAccess(_F)
if mibBuilder.loadTexts:osL2PduGuardSupprt.setStatus(_A)
_OsL2PduGuardTable_Object=MibTable
osL2PduGuardTable=_OsL2PduGuardTable_Object((1,3,6,1,4,1,6926,2,17,2))
if mibBuilder.loadTexts:osL2PduGuardTable.setStatus(_A)
_OsL2PduGuardEntry_Object=MibTableRow
osL2PduGuardEntry=_OsL2PduGuardEntry_Object((1,3,6,1,4,1,6926,2,17,2,1))
osL2PduGuardEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:osL2PduGuardEntry.setStatus(_A)
_OsL2PduGuardProtocol_Type=L2ProtocolId
_OsL2PduGuardProtocol_Object=MibTableColumn
osL2PduGuardProtocol=_OsL2PduGuardProtocol_Object((1,3,6,1,4,1,6926,2,17,2,1,1),_OsL2PduGuardProtocol_Type())
osL2PduGuardProtocol.setMaxAccess(_I)
if mibBuilder.loadTexts:osL2PduGuardProtocol.setStatus(_A)
class _OsL2PduGuardPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OsL2PduGuardPort_Type.__name__=_D
_OsL2PduGuardPort_Object=MibTableColumn
osL2PduGuardPort=_OsL2PduGuardPort_Object((1,3,6,1,4,1,6926,2,17,2,1,2),_OsL2PduGuardPort_Type())
osL2PduGuardPort.setMaxAccess(_I)
if mibBuilder.loadTexts:osL2PduGuardPort.setStatus(_A)
class _OsL2PduGuardIsolateRate_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,300))
_OsL2PduGuardIsolateRate_Type.__name__=_C
_OsL2PduGuardIsolateRate_Object=MibTableColumn
osL2PduGuardIsolateRate=_OsL2PduGuardIsolateRate_Object((1,3,6,1,4,1,6926,2,17,2,1,3),_OsL2PduGuardIsolateRate_Type())
osL2PduGuardIsolateRate.setMaxAccess(_J)
if mibBuilder.loadTexts:osL2PduGuardIsolateRate.setStatus(_A)
if mibBuilder.loadTexts:osL2PduGuardIsolateRate.setUnits(_K)
class _OsL2PduGuardInformRate_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,300))
_OsL2PduGuardInformRate_Type.__name__=_C
_OsL2PduGuardInformRate_Object=MibTableColumn
osL2PduGuardInformRate=_OsL2PduGuardInformRate_Object((1,3,6,1,4,1,6926,2,17,2,1,4),_OsL2PduGuardInformRate_Type())
osL2PduGuardInformRate.setMaxAccess(_J)
if mibBuilder.loadTexts:osL2PduGuardInformRate.setStatus(_A)
if mibBuilder.loadTexts:osL2PduGuardInformRate.setUnits(_K)
_OsL2PduGuardState_Type=L2PortState
_OsL2PduGuardState_Object=MibTableColumn
osL2PduGuardState=_OsL2PduGuardState_Object((1,3,6,1,4,1,6926,2,17,2,1,5),_OsL2PduGuardState_Type())
osL2PduGuardState.setMaxAccess(_F)
if mibBuilder.loadTexts:osL2PduGuardState.setStatus(_A)
_OsL2PduGuardCpConformance_ObjectIdentity=ObjectIdentity
osL2PduGuardCpConformance=_OsL2PduGuardCpConformance_ObjectIdentity((1,3,6,1,4,1,6926,2,17,100))
_OsL2PduGuardCpMIBCompliances_ObjectIdentity=ObjectIdentity
osL2PduGuardCpMIBCompliances=_OsL2PduGuardCpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,17,100,1))
_OsL2PduGuardCpMIBGroups_ObjectIdentity=ObjectIdentity
osL2PduGuardCpMIBGroups=_OsL2PduGuardCpMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,17,100,2))
osL2PduGuardMandatoryGroup=ObjectGroup((1,3,6,1,4,1,6926,2,17,100,2,1))
osL2PduGuardMandatoryGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:osL2PduGuardMandatoryGroup.setStatus(_A)
osL2PduGuardCpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,17,100,1,1))
osL2PduGuardCpMIBCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:osL2PduGuardCpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'L2ProtocolId':L2ProtocolId,'L2PortState':L2PortState,'SupportValue':SupportValue,'osL2PduGuard':osL2PduGuard,'osL2PduGuardCpGen':osL2PduGuardCpGen,_L:osL2PduGuardSupprt,'osL2PduGuardTable':osL2PduGuardTable,'osL2PduGuardEntry':osL2PduGuardEntry,_G:osL2PduGuardProtocol,_H:osL2PduGuardPort,_M:osL2PduGuardIsolateRate,_N:osL2PduGuardInformRate,_O:osL2PduGuardState,'osL2PduGuardCpConformance':osL2PduGuardCpConformance,'osL2PduGuardCpMIBCompliances':osL2PduGuardCpMIBCompliances,'osL2PduGuardCpMIBCompliance':osL2PduGuardCpMIBCompliance,'osL2PduGuardCpMIBGroups':osL2PduGuardCpMIBGroups,_P:osL2PduGuardMandatoryGroup})