_O='cmmOcgPtpGroup'
_N='cmmOcgPtpProvisionedOcgNumber'
_M='cmmOcgPtpOcgPowerControlLoop'
_L='cmmOcgPtpPmHistStatsEnable'
_K='cmmOcgPtpAutoDiscoveryState'
_J='cmmOcgPtpDiscoveredRemoteTP'
_I='read-write'
_H='disabled'
_G='enabled'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='Integer32'
_B='INFINERA-TP-CMMOCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cmmOcgPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,28))
if mibBuilder.loadTexts:cmmOcgPtpMIB.setRevisions(('2008-10-20 00:00',))
_CmmOcgPtpTable_Object=MibTable
cmmOcgPtpTable=_CmmOcgPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,28,1))
if mibBuilder.loadTexts:cmmOcgPtpTable.setStatus(_A)
_CmmOcgPtpEntry_Object=MibTableRow
cmmOcgPtpEntry=_CmmOcgPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,28,1,1))
cmmOcgPtpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cmmOcgPtpEntry.setStatus(_A)
_CmmOcgPtpDiscoveredRemoteTP_Type=DisplayString
_CmmOcgPtpDiscoveredRemoteTP_Object=MibTableColumn
cmmOcgPtpDiscoveredRemoteTP=_CmmOcgPtpDiscoveredRemoteTP_Object((1,3,6,1,4,1,21296,2,2,2,2,28,1,1,1),_CmmOcgPtpDiscoveredRemoteTP_Type())
cmmOcgPtpDiscoveredRemoteTP.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmOcgPtpDiscoveredRemoteTP.setStatus(_A)
class _CmmOcgPtpAutoDiscoveryState_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('inProgress',1),('completed',2),('unknown',3),('notValidOrShutdown',4),('failed',5)))
_CmmOcgPtpAutoDiscoveryState_Type.__name__=_C
_CmmOcgPtpAutoDiscoveryState_Object=MibTableColumn
cmmOcgPtpAutoDiscoveryState=_CmmOcgPtpAutoDiscoveryState_Object((1,3,6,1,4,1,21296,2,2,2,2,28,1,1,2),_CmmOcgPtpAutoDiscoveryState_Type())
cmmOcgPtpAutoDiscoveryState.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmOcgPtpAutoDiscoveryState.setStatus(_A)
class _CmmOcgPtpPmHistStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CmmOcgPtpPmHistStatsEnable_Type.__name__=_C
_CmmOcgPtpPmHistStatsEnable_Object=MibTableColumn
cmmOcgPtpPmHistStatsEnable=_CmmOcgPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,28,1,1,3),_CmmOcgPtpPmHistStatsEnable_Type())
cmmOcgPtpPmHistStatsEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:cmmOcgPtpPmHistStatsEnable.setStatus(_A)
class _CmmOcgPtpOperatingMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('gen1',1),('gen2',2)))
_CmmOcgPtpOperatingMode_Type.__name__=_C
_CmmOcgPtpOperatingMode_Object=MibTableColumn
cmmOcgPtpOperatingMode=_CmmOcgPtpOperatingMode_Object((1,3,6,1,4,1,21296,2,2,2,2,28,1,1,4),_CmmOcgPtpOperatingMode_Type())
cmmOcgPtpOperatingMode.setMaxAccess('read-create')
if mibBuilder.loadTexts:cmmOcgPtpOperatingMode.setStatus(_A)
class _CmmOcgPtpOcgPowerControlLoop_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_CmmOcgPtpOcgPowerControlLoop_Type.__name__=_C
_CmmOcgPtpOcgPowerControlLoop_Object=MibTableColumn
cmmOcgPtpOcgPowerControlLoop=_CmmOcgPtpOcgPowerControlLoop_Object((1,3,6,1,4,1,21296,2,2,2,2,28,1,1,5),_CmmOcgPtpOcgPowerControlLoop_Type())
cmmOcgPtpOcgPowerControlLoop.setMaxAccess(_I)
if mibBuilder.loadTexts:cmmOcgPtpOcgPowerControlLoop.setStatus(_A)
class _CmmOcgPtpProvisionedOcgNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CmmOcgPtpProvisionedOcgNumber_Type.__name__=_C
_CmmOcgPtpProvisionedOcgNumber_Object=MibTableColumn
cmmOcgPtpProvisionedOcgNumber=_CmmOcgPtpProvisionedOcgNumber_Object((1,3,6,1,4,1,21296,2,2,2,2,28,1,1,6),_CmmOcgPtpProvisionedOcgNumber_Type())
cmmOcgPtpProvisionedOcgNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmOcgPtpProvisionedOcgNumber.setStatus(_A)
_CmmOcgPtpConformance_ObjectIdentity=ObjectIdentity
cmmOcgPtpConformance=_CmmOcgPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,28,3))
_CmmOcgPtpCompliances_ObjectIdentity=ObjectIdentity
cmmOcgPtpCompliances=_CmmOcgPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,28,3,1))
_CmmOcgPtpGroups_ObjectIdentity=ObjectIdentity
cmmOcgPtpGroups=_CmmOcgPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,28,3,2))
cmmOcgPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,28,3,2,1))
cmmOcgPtpGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:cmmOcgPtpGroup.setStatus(_A)
cmmOcgPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,28,3,1,1))
cmmOcgPtpCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:cmmOcgPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cmmOcgPtpMIB':cmmOcgPtpMIB,'cmmOcgPtpTable':cmmOcgPtpTable,'cmmOcgPtpEntry':cmmOcgPtpEntry,_J:cmmOcgPtpDiscoveredRemoteTP,_K:cmmOcgPtpAutoDiscoveryState,_L:cmmOcgPtpPmHistStatsEnable,'cmmOcgPtpOperatingMode':cmmOcgPtpOperatingMode,_M:cmmOcgPtpOcgPowerControlLoop,_N:cmmOcgPtpProvisionedOcgNumber,'cmmOcgPtpConformance':cmmOcgPtpConformance,'cmmOcgPtpCompliances':cmmOcgPtpCompliances,'cmmOcgPtpCompliance':cmmOcgPtpCompliance,'cmmOcgPtpGroups':cmmOcgPtpGroups,_O:cmmOcgPtpGroup})