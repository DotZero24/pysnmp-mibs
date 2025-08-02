_h='ssrTrapsConfGroupV50'
_g='ssrTrapsConfGroupV40'
_f='ssrTrapsConfGroupV30'
_e='ssrTrapsConfGroupV20'
_d='ssrTrapsConfGroupV10'
_c='polAclDenied'
_b='obsolete'
_a='ifIndex'
_Z='IF-MIB'
_Y='polAclName'
_X='polAclItem'
_W='capCPUCurrentUtilization'
_V='CTRON-SSR-CAPACITY-MIB'
_U='envCPUThresholdExceeded'
_T='envLineModuleFailure'
_S='envBackupControlModuleFailure'
_R='envBackupControlModuleOnline'
_Q='CTRON-SSR-POLICY-MIB'
_P='sysHwTemperature'
_O='sysHwPowerSupply'
_N='sysHwFan'
_M='envHotSwapOut'
_L='envHotSwapIn'
_K='deprecated'
_J='envTempNormal'
_I='envTempExceeded'
_H='envFanRecovered'
_G='envFanFailed'
_F='envPowerSupplyRecovered'
_E='envPowerSupplyFailed'
_D='sysHwModuleSlotNumber'
_C='CTRON-SSR-HARDWARE-MIB'
_B='current'
_A='CTRON-SSR-TRAP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
capCPUCurrentUtilization,=mibBuilder.importSymbols(_V,_W)
sysHwFan,sysHwModuleSlotNumber,sysHwPowerSupply,sysHwTemperature=mibBuilder.importSymbols(_C,_N,_D,_O,_P)
polAclItem,polAclName=mibBuilder.importSymbols(_Q,_X,_Y)
ssrMibs,ssrTraps=mibBuilder.importSymbols('CTRON-SSR-SMI-MIB','ssrMibs','ssrTraps')
ifIndex,=mibBuilder.importSymbols(_Z,_a)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ssrTrapsMIB=ModuleIdentity((1,3,6,1,4,1,52,2501,1,300))
if mibBuilder.loadTexts:ssrTrapsMIB.setRevisions(('2002-07-23 17:20','2001-02-16 00:00'))
_SsrTrapsConformance_ObjectIdentity=ObjectIdentity
ssrTrapsConformance=_SsrTrapsConformance_ObjectIdentity((1,3,6,1,4,1,52,2501,1,300,2))
_SsrTrapsCompliances_ObjectIdentity=ObjectIdentity
ssrTrapsCompliances=_SsrTrapsCompliances_ObjectIdentity((1,3,6,1,4,1,52,2501,1,300,2,1))
_SsrTrapsGroups_ObjectIdentity=ObjectIdentity
ssrTrapsGroups=_SsrTrapsGroups_ObjectIdentity((1,3,6,1,4,1,52,2501,1,300,2,2))
_TrapControl_ObjectIdentity=ObjectIdentity
trapControl=_TrapControl_ObjectIdentity((1,3,6,1,4,1,52,2501,10,1))
_EnvTrapGroup_ObjectIdentity=ObjectIdentity
envTrapGroup=_EnvTrapGroup_ObjectIdentity((1,3,6,1,4,1,52,2501,10,2))
_PolTrapGroup_ObjectIdentity=ObjectIdentity
polTrapGroup=_PolTrapGroup_ObjectIdentity((1,3,6,1,4,1,52,2501,10,3))
_PolNotifications_ObjectIdentity=ObjectIdentity
polNotifications=_PolNotifications_ObjectIdentity((1,3,6,1,4,1,52,2501,10,3,0))
envPowerSupplyFailed=NotificationType((1,3,6,1,4,1,52,2501,10,2,1))
envPowerSupplyFailed.setObjects((_C,_O))
if mibBuilder.loadTexts:envPowerSupplyFailed.setStatus(_B)
envPowerSupplyRecovered=NotificationType((1,3,6,1,4,1,52,2501,10,2,2))
envPowerSupplyRecovered.setObjects((_C,_O))
if mibBuilder.loadTexts:envPowerSupplyRecovered.setStatus(_B)
envFanFailed=NotificationType((1,3,6,1,4,1,52,2501,10,2,3))
envFanFailed.setObjects((_C,_N))
if mibBuilder.loadTexts:envFanFailed.setStatus(_B)
envFanRecovered=NotificationType((1,3,6,1,4,1,52,2501,10,2,4))
envFanRecovered.setObjects((_C,_N))
if mibBuilder.loadTexts:envFanRecovered.setStatus(_B)
envTempExceeded=NotificationType((1,3,6,1,4,1,52,2501,10,2,5))
envTempExceeded.setObjects((_C,_P))
if mibBuilder.loadTexts:envTempExceeded.setStatus(_B)
envTempNormal=NotificationType((1,3,6,1,4,1,52,2501,10,2,6))
envTempNormal.setObjects((_C,_P))
if mibBuilder.loadTexts:envTempNormal.setStatus(_B)
envHotSwapIn=NotificationType((1,3,6,1,4,1,52,2501,10,2,7))
envHotSwapIn.setObjects((_C,_D))
if mibBuilder.loadTexts:envHotSwapIn.setStatus(_B)
envHotSwapOut=NotificationType((1,3,6,1,4,1,52,2501,10,2,8))
envHotSwapOut.setObjects((_C,_D))
if mibBuilder.loadTexts:envHotSwapOut.setStatus(_B)
envBackupControlModuleOnline=NotificationType((1,3,6,1,4,1,52,2501,10,2,9))
envBackupControlModuleOnline.setObjects((_C,_D))
if mibBuilder.loadTexts:envBackupControlModuleOnline.setStatus(_B)
envBackupControlModuleFailure=NotificationType((1,3,6,1,4,1,52,2501,10,2,10))
envBackupControlModuleFailure.setObjects((_C,_D))
if mibBuilder.loadTexts:envBackupControlModuleFailure.setStatus(_B)
envLineModuleFailure=NotificationType((1,3,6,1,4,1,52,2501,10,2,11))
envLineModuleFailure.setObjects((_C,_D))
if mibBuilder.loadTexts:envLineModuleFailure.setStatus(_B)
envCPUThresholdExceeded=NotificationType((1,3,6,1,4,1,52,2501,10,2,12))
envCPUThresholdExceeded.setObjects(*((_C,_D),(_V,_W)))
if mibBuilder.loadTexts:envCPUThresholdExceeded.setStatus(_B)
polAclDenied=NotificationType((1,3,6,1,4,1,52,2501,10,3,0,1))
polAclDenied.setObjects(*((_Q,_Y),(_Q,_X),(_Z,_a)))
if mibBuilder.loadTexts:polAclDenied.setStatus(_B)
ssrTrapsConfGroupV10=NotificationGroup((1,3,6,1,4,1,52,2501,1,300,2,2,1))
ssrTrapsConfGroupV10.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:ssrTrapsConfGroupV10.setStatus(_b)
ssrTrapsConfGroupV20=NotificationGroup((1,3,6,1,4,1,52,2501,1,300,2,2,2))
ssrTrapsConfGroupV20.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:ssrTrapsConfGroupV20.setStatus(_K)
ssrTrapsConfGroupV30=NotificationGroup((1,3,6,1,4,1,52,2501,1,300,2,2,3))
ssrTrapsConfGroupV30.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:ssrTrapsConfGroupV30.setStatus(_K)
ssrTrapsConfGroupV40=NotificationGroup((1,3,6,1,4,1,52,2501,1,300,2,2,4))
ssrTrapsConfGroupV40.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_L),(_A,_M),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:ssrTrapsConfGroupV40.setStatus(_K)
ssrTrapsConfGroupV50=NotificationGroup((1,3,6,1,4,1,52,2501,1,300,2,2,5))
ssrTrapsConfGroupV50.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_L),(_A,_M),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_c)))
if mibBuilder.loadTexts:ssrTrapsConfGroupV50.setStatus(_B)
ssrTrapsComplianceV10=ModuleCompliance((1,3,6,1,4,1,52,2501,1,300,2,2,1,1))
ssrTrapsComplianceV10.setObjects((_A,_d))
if mibBuilder.loadTexts:ssrTrapsComplianceV10.setStatus(_b)
ssrTrapsComplianceV20=ModuleCompliance((1,3,6,1,4,1,52,2501,1,300,2,2,2,1))
ssrTrapsComplianceV20.setObjects((_A,_e))
if mibBuilder.loadTexts:ssrTrapsComplianceV20.setStatus(_K)
ssrTrapsComplianceV30=ModuleCompliance((1,3,6,1,4,1,52,2501,1,300,2,2,3,1))
ssrTrapsComplianceV30.setObjects((_A,_f))
if mibBuilder.loadTexts:ssrTrapsComplianceV30.setStatus(_K)
ssrTrapsComplianceV40=ModuleCompliance((1,3,6,1,4,1,52,2501,1,300,2,2,4,1))
ssrTrapsComplianceV40.setObjects((_A,_g))
if mibBuilder.loadTexts:ssrTrapsComplianceV40.setStatus(_B)
ssrTrapsComplianceV50=ModuleCompliance((1,3,6,1,4,1,52,2501,1,300,2,2,5,1))
ssrTrapsComplianceV50.setObjects((_A,_h))
if mibBuilder.loadTexts:ssrTrapsComplianceV50.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ssrTrapsMIB':ssrTrapsMIB,'ssrTrapsConformance':ssrTrapsConformance,'ssrTrapsCompliances':ssrTrapsCompliances,'ssrTrapsGroups':ssrTrapsGroups,_d:ssrTrapsConfGroupV10,'ssrTrapsComplianceV10':ssrTrapsComplianceV10,_e:ssrTrapsConfGroupV20,'ssrTrapsComplianceV20':ssrTrapsComplianceV20,_f:ssrTrapsConfGroupV30,'ssrTrapsComplianceV30':ssrTrapsComplianceV30,_g:ssrTrapsConfGroupV40,'ssrTrapsComplianceV40':ssrTrapsComplianceV40,_h:ssrTrapsConfGroupV50,'ssrTrapsComplianceV50':ssrTrapsComplianceV50,'trapControl':trapControl,'envTrapGroup':envTrapGroup,_E:envPowerSupplyFailed,_F:envPowerSupplyRecovered,_G:envFanFailed,_H:envFanRecovered,_I:envTempExceeded,_J:envTempNormal,_L:envHotSwapIn,_M:envHotSwapOut,_R:envBackupControlModuleOnline,_S:envBackupControlModuleFailure,_T:envLineModuleFailure,_U:envCPUThresholdExceeded,'polTrapGroup':polTrapGroup,'polNotifications':polNotifications,_c:polAclDenied})