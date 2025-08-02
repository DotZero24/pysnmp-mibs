_Z='dlmOcgPtpGroup'
_Y='dlmOcgPtpAggregateRate'
_X='dlmOcgPtpChannelCount'
_W='dlmOcgPtpOpenwaveTargetTxOcgPower'
_V='dlmOcgPtpProvisionedPeerTP'
_U='dlmOcgPtpLineSystemMode'
_T='dlmOcgPtpDiscoveredOcgTP'
_S='dlmOcgPtpProvisionedOcgTP'
_R='dlmOcgPtpOcgPowerControlLoop'
_Q='dlmOcgPtpIsBorderOCG'
_P='dlmOcgPtpPmHistStatsEnable'
_O='dlmOcgPtpAutoDiscoveryState'
_N='dlmOcgPtpDiscoveredRemoteTP'
_M='obsolete'
_L='TruthValue'
_K='InfnPmHistStatsControl'
_J='InfnOperationalState'
_I='InfnLineSystemMode'
_H='InfnAutoDiscoveryState'
_G='ifIndex'
_F='IF-MIB'
_E='read-only'
_D='FloatTenths'
_C='read-write'
_B='INFINERA-TP-DLMOCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatTenths,InfnAutoDiscoveryState,InfnLineSystemMode,InfnOperationalState,InfnPmHistStatsControl=mibBuilder.importSymbols('INFINERA-TC-MIB',_D,_H,_I,_J,_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_L)
dlmOcgPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,6))
if mibBuilder.loadTexts:dlmOcgPtpMIB.setRevisions(('2008-10-20 00:00',))
_DlmOcgPtpTable_Object=MibTable
dlmOcgPtpTable=_DlmOcgPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,6,1))
if mibBuilder.loadTexts:dlmOcgPtpTable.setStatus(_A)
_DlmOcgPtpEntry_Object=MibTableRow
dlmOcgPtpEntry=_DlmOcgPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,6,1,1))
dlmOcgPtpEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dlmOcgPtpEntry.setStatus(_A)
_DlmOcgPtpDiscoveredRemoteTP_Type=DisplayString
_DlmOcgPtpDiscoveredRemoteTP_Object=MibTableColumn
dlmOcgPtpDiscoveredRemoteTP=_DlmOcgPtpDiscoveredRemoteTP_Object((1,3,6,1,4,1,21296,2,2,2,2,6,1,1,1),_DlmOcgPtpDiscoveredRemoteTP_Type())
dlmOcgPtpDiscoveredRemoteTP.setMaxAccess(_E)
if mibBuilder.loadTexts:dlmOcgPtpDiscoveredRemoteTP.setStatus(_A)
class _DlmOcgPtpAutoDiscoveryState_Type(InfnAutoDiscoveryState):defaultValue=4
_DlmOcgPtpAutoDiscoveryState_Type.__name__=_H
_DlmOcgPtpAutoDiscoveryState_Object=MibTableColumn
dlmOcgPtpAutoDiscoveryState=_DlmOcgPtpAutoDiscoveryState_Object((1,3,6,1,4,1,21296,2,2,2,2,6,1,1,2),_DlmOcgPtpAutoDiscoveryState_Type())
dlmOcgPtpAutoDiscoveryState.setMaxAccess(_E)
if mibBuilder.loadTexts:dlmOcgPtpAutoDiscoveryState.setStatus(_A)
class _DlmOcgPtpPmHistStatsEnable_Type(InfnPmHistStatsControl):defaultValue=1
_DlmOcgPtpPmHistStatsEnable_Type.__name__=_K
_DlmOcgPtpPmHistStatsEnable_Object=MibTableColumn
dlmOcgPtpPmHistStatsEnable=_DlmOcgPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,6,1,1,3),_DlmOcgPtpPmHistStatsEnable_Type())
dlmOcgPtpPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dlmOcgPtpPmHistStatsEnable.setStatus(_M)
class _DlmOcgPtpIsBorderOCG_Type(TruthValue):defaultValue=2
_DlmOcgPtpIsBorderOCG_Type.__name__=_L
_DlmOcgPtpIsBorderOCG_Object=MibTableColumn
dlmOcgPtpIsBorderOCG=_DlmOcgPtpIsBorderOCG_Object((1,3,6,1,4,1,21296,2,2,2,2,6,1,1,4),_DlmOcgPtpIsBorderOCG_Type())
dlmOcgPtpIsBorderOCG.setMaxAccess(_C)
if mibBuilder.loadTexts:dlmOcgPtpIsBorderOCG.setStatus(_M)
class _DlmOcgPtpOcgPowerControlLoop_Type(InfnOperationalState):defaultValue=2
_DlmOcgPtpOcgPowerControlLoop_Type.__name__=_J
_DlmOcgPtpOcgPowerControlLoop_Object=MibTableColumn
dlmOcgPtpOcgPowerControlLoop=_DlmOcgPtpOcgPowerControlLoop_Object((1,3,6,1,4,1,21296,2,2,2,2,6,1,1,5),_DlmOcgPtpOcgPowerControlLoop_Type())
dlmOcgPtpOcgPowerControlLoop.setMaxAccess(_C)
if mibBuilder.loadTexts:dlmOcgPtpOcgPowerControlLoop.setStatus(_A)
_DlmOcgPtpProvisionedOcgTP_Type=DisplayString
_DlmOcgPtpProvisionedOcgTP_Object=MibTableColumn
dlmOcgPtpProvisionedOcgTP=_DlmOcgPtpProvisionedOcgTP_Object((1,3,6,1,4,1,21296,2,2,2,2,6,1,1,6),_DlmOcgPtpProvisionedOcgTP_Type())
dlmOcgPtpProvisionedOcgTP.setMaxAccess(_C)
if mibBuilder.loadTexts:dlmOcgPtpProvisionedOcgTP.setStatus(_A)
_DlmOcgPtpDiscoveredOcgTP_Type=DisplayString
_DlmOcgPtpDiscoveredOcgTP_Object=MibTableColumn
dlmOcgPtpDiscoveredOcgTP=_DlmOcgPtpDiscoveredOcgTP_Object((1,3,6,1,4,1,21296,2,2,2,2,6,1,1,7),_DlmOcgPtpDiscoveredOcgTP_Type())
dlmOcgPtpDiscoveredOcgTP.setMaxAccess(_E)
if mibBuilder.loadTexts:dlmOcgPtpDiscoveredOcgTP.setStatus(_A)
class _DlmOcgPtpLineSystemMode_Type(InfnLineSystemMode):defaultValue=1
_DlmOcgPtpLineSystemMode_Type.__name__=_I
_DlmOcgPtpLineSystemMode_Object=MibTableColumn
dlmOcgPtpLineSystemMode=_DlmOcgPtpLineSystemMode_Object((1,3,6,1,4,1,21296,2,2,2,2,6,1,1,8),_DlmOcgPtpLineSystemMode_Type())
dlmOcgPtpLineSystemMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dlmOcgPtpLineSystemMode.setStatus(_A)
_DlmOcgPtpProvisionedPeerTP_Type=DisplayString
_DlmOcgPtpProvisionedPeerTP_Object=MibTableColumn
dlmOcgPtpProvisionedPeerTP=_DlmOcgPtpProvisionedPeerTP_Object((1,3,6,1,4,1,21296,2,2,2,2,6,1,1,9),_DlmOcgPtpProvisionedPeerTP_Type())
dlmOcgPtpProvisionedPeerTP.setMaxAccess(_C)
if mibBuilder.loadTexts:dlmOcgPtpProvisionedPeerTP.setStatus(_A)
class _DlmOcgPtpOpenwaveTargetTxOcgPower_Type(FloatTenths):defaultValue=50
_DlmOcgPtpOpenwaveTargetTxOcgPower_Type.__name__=_D
_DlmOcgPtpOpenwaveTargetTxOcgPower_Object=MibTableColumn
dlmOcgPtpOpenwaveTargetTxOcgPower=_DlmOcgPtpOpenwaveTargetTxOcgPower_Object((1,3,6,1,4,1,21296,2,2,2,2,6,1,1,10),_DlmOcgPtpOpenwaveTargetTxOcgPower_Type())
dlmOcgPtpOpenwaveTargetTxOcgPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dlmOcgPtpOpenwaveTargetTxOcgPower.setStatus(_A)
class _DlmOcgPtpChannelCount_Type(FloatTenths):defaultValue=100
_DlmOcgPtpChannelCount_Type.__name__=_D
_DlmOcgPtpChannelCount_Object=MibTableColumn
dlmOcgPtpChannelCount=_DlmOcgPtpChannelCount_Object((1,3,6,1,4,1,21296,2,2,2,2,6,1,1,11),_DlmOcgPtpChannelCount_Type())
dlmOcgPtpChannelCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dlmOcgPtpChannelCount.setStatus(_A)
class _DlmOcgPtpAggregateRate_Type(FloatTenths):defaultValue=500
_DlmOcgPtpAggregateRate_Type.__name__=_D
_DlmOcgPtpAggregateRate_Object=MibTableColumn
dlmOcgPtpAggregateRate=_DlmOcgPtpAggregateRate_Object((1,3,6,1,4,1,21296,2,2,2,2,6,1,1,12),_DlmOcgPtpAggregateRate_Type())
dlmOcgPtpAggregateRate.setMaxAccess(_E)
if mibBuilder.loadTexts:dlmOcgPtpAggregateRate.setStatus(_A)
_DlmOcgPtpConformance_ObjectIdentity=ObjectIdentity
dlmOcgPtpConformance=_DlmOcgPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,6,3))
_DlmOcgPtpCompliances_ObjectIdentity=ObjectIdentity
dlmOcgPtpCompliances=_DlmOcgPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,6,3,1))
_DlmOcgPtpGroups_ObjectIdentity=ObjectIdentity
dlmOcgPtpGroups=_DlmOcgPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,6,3,2))
dlmOcgPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,6,3,2,1))
dlmOcgPtpGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:dlmOcgPtpGroup.setStatus(_A)
dlmOcgPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,6,3,1,1))
dlmOcgPtpCompliance.setObjects((_B,_Z))
if mibBuilder.loadTexts:dlmOcgPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlmOcgPtpMIB':dlmOcgPtpMIB,'dlmOcgPtpTable':dlmOcgPtpTable,'dlmOcgPtpEntry':dlmOcgPtpEntry,_N:dlmOcgPtpDiscoveredRemoteTP,_O:dlmOcgPtpAutoDiscoveryState,_P:dlmOcgPtpPmHistStatsEnable,_Q:dlmOcgPtpIsBorderOCG,_R:dlmOcgPtpOcgPowerControlLoop,_S:dlmOcgPtpProvisionedOcgTP,_T:dlmOcgPtpDiscoveredOcgTP,_U:dlmOcgPtpLineSystemMode,_V:dlmOcgPtpProvisionedPeerTP,_W:dlmOcgPtpOpenwaveTargetTxOcgPower,_X:dlmOcgPtpChannelCount,_Y:dlmOcgPtpAggregateRate,'dlmOcgPtpConformance':dlmOcgPtpConformance,'dlmOcgPtpCompliances':dlmOcgPtpCompliances,'dlmOcgPtpCompliance':dlmOcgPtpCompliance,'dlmOcgPtpGroups':dlmOcgPtpGroups,_Z:dlmOcgPtpGroup})