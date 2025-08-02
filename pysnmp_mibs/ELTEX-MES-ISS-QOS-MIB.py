_R='eltMesIssQoSCpuRateLimitEntry'
_Q='eltMesIssQoSMeterEntry'
_P='not-accessible'
_O='eltMesIssQoSIfUtilizationInterval'
_N='eltMesIssQoSIfUtilizationIfIndex'
_M='EltMesIssQoSRemarkPortDefaultCosSource'
_L='EltMesIssQoSTrustMode'
_K='EltMesIssMeterUnits'
_J='fsQosHwCpuQId'
_I='fsQosHwCpuMaxRate'
_H='ifIndex'
_G='IF-MIB'
_F='ARICENT-QOS-MIB'
_E='read-only'
_D='ELTEX-MES-ISS-QOS-MIB'
_C='TruthValue'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsQoSMeterEntry,fsQosHwCpuMaxRate,fsQosHwCpuQId,fsQosHwCpuRateLimitEntry=mibBuilder.importSymbols(_F,'fsQoSMeterEntry',_I,_J,'fsQosHwCpuRateLimitEntry')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_C)
eltMesIssQoSMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,5))
if mibBuilder.loadTexts:eltMesIssQoSMIB.setRevisions(('2019-01-18 00:00','2018-12-18 00:00'))
class EltMesIssQoSTrustMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('cos',2),('dscp',3),('cos-dscp',4)))
class EltMesIssMeterUnits(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bytes',1),('packets',2)))
class EltMesIssQoSRemarkPortDefaultCosSource(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('user-priority',2),('inner-vlanPri',3)))
_EltMesIssQoSObjects_ObjectIdentity=ObjectIdentity
eltMesIssQoSObjects=_EltMesIssQoSObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,5,1))
_EltMesIssQoSGlobals_ObjectIdentity=ObjectIdentity
eltMesIssQoSGlobals=_EltMesIssQoSGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,139,5,1,1))
_EltMesIssQoSTrustMode_Type=EltMesIssQoSTrustMode
_EltMesIssQoSTrustMode_Object=MibScalar
eltMesIssQoSTrustMode=_EltMesIssQoSTrustMode_Object((1,3,6,1,4,1,35265,1,139,5,1,1,1),_EltMesIssQoSTrustMode_Type())
eltMesIssQoSTrustMode.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssQoSTrustMode.setStatus(_A)
_EltMesIssQoSMetering_ObjectIdentity=ObjectIdentity
eltMesIssQoSMetering=_EltMesIssQoSMetering_ObjectIdentity((1,3,6,1,4,1,35265,1,139,5,1,2))
_EltMesIssQoSMeterTable_Object=MibTable
eltMesIssQoSMeterTable=_EltMesIssQoSMeterTable_Object((1,3,6,1,4,1,35265,1,139,5,1,2,1))
if mibBuilder.loadTexts:eltMesIssQoSMeterTable.setStatus(_A)
_EltMesIssQoSMeterEntry_Object=MibTableRow
eltMesIssQoSMeterEntry=_EltMesIssQoSMeterEntry_Object((1,3,6,1,4,1,35265,1,139,5,1,2,1,1))
if mibBuilder.loadTexts:eltMesIssQoSMeterEntry.setStatus(_A)
class _EltMesIssQoSMeterUnits_Type(EltMesIssMeterUnits):defaultValue=1
_EltMesIssQoSMeterUnits_Type.__name__=_K
_EltMesIssQoSMeterUnits_Object=MibTableColumn
eltMesIssQoSMeterUnits=_EltMesIssQoSMeterUnits_Object((1,3,6,1,4,1,35265,1,139,5,1,2,1,1,1),_EltMesIssQoSMeterUnits_Type())
eltMesIssQoSMeterUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssQoSMeterUnits.setStatus(_A)
_EltMesIssQoSTrafficMgmt_ObjectIdentity=ObjectIdentity
eltMesIssQoSTrafficMgmt=_EltMesIssQoSTrafficMgmt_ObjectIdentity((1,3,6,1,4,1,35265,1,139,5,1,3))
_EltMesIssQoSPortTrustModeTable_Object=MibTable
eltMesIssQoSPortTrustModeTable=_EltMesIssQoSPortTrustModeTable_Object((1,3,6,1,4,1,35265,1,139,5,1,3,1))
if mibBuilder.loadTexts:eltMesIssQoSPortTrustModeTable.setStatus(_A)
_EltMesIssQoSPortTrustModeEntry_Object=MibTableRow
eltMesIssQoSPortTrustModeEntry=_EltMesIssQoSPortTrustModeEntry_Object((1,3,6,1,4,1,35265,1,139,5,1,3,1,1))
eltMesIssQoSPortTrustModeEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:eltMesIssQoSPortTrustModeEntry.setStatus(_A)
class _EltMesIssQoSPortTrustMode_Type(EltMesIssQoSTrustMode):defaultValue=1
_EltMesIssQoSPortTrustMode_Type.__name__=_L
_EltMesIssQoSPortTrustMode_Object=MibTableColumn
eltMesIssQoSPortTrustMode=_EltMesIssQoSPortTrustMode_Object((1,3,6,1,4,1,35265,1,139,5,1,3,1,1,1),_EltMesIssQoSPortTrustMode_Type())
eltMesIssQoSPortTrustMode.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssQoSPortTrustMode.setStatus(_A)
_EltMesIssQoSRemarking_ObjectIdentity=ObjectIdentity
eltMesIssQoSRemarking=_EltMesIssQoSRemarking_ObjectIdentity((1,3,6,1,4,1,35265,1,139,5,1,4))
_EltMesIssQoSRemarkPortTable_Object=MibTable
eltMesIssQoSRemarkPortTable=_EltMesIssQoSRemarkPortTable_Object((1,3,6,1,4,1,35265,1,139,5,1,4,1))
if mibBuilder.loadTexts:eltMesIssQoSRemarkPortTable.setStatus(_A)
_EltMesIssQoSRemarkPortEntry_Object=MibTableRow
eltMesIssQoSRemarkPortEntry=_EltMesIssQoSRemarkPortEntry_Object((1,3,6,1,4,1,35265,1,139,5,1,4,1,1))
eltMesIssQoSRemarkPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:eltMesIssQoSRemarkPortEntry.setStatus(_A)
class _EltMesIssQoSRemarkPortCosEnable_Type(TruthValue):defaultValue=2
_EltMesIssQoSRemarkPortCosEnable_Type.__name__=_C
_EltMesIssQoSRemarkPortCosEnable_Object=MibTableColumn
eltMesIssQoSRemarkPortCosEnable=_EltMesIssQoSRemarkPortCosEnable_Object((1,3,6,1,4,1,35265,1,139,5,1,4,1,1,1),_EltMesIssQoSRemarkPortCosEnable_Type())
eltMesIssQoSRemarkPortCosEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssQoSRemarkPortCosEnable.setStatus(_A)
class _EltMesIssQoSRemarkPortDscpEnable_Type(TruthValue):defaultValue=2
_EltMesIssQoSRemarkPortDscpEnable_Type.__name__=_C
_EltMesIssQoSRemarkPortDscpEnable_Object=MibTableColumn
eltMesIssQoSRemarkPortDscpEnable=_EltMesIssQoSRemarkPortDscpEnable_Object((1,3,6,1,4,1,35265,1,139,5,1,4,1,1,2),_EltMesIssQoSRemarkPortDscpEnable_Type())
eltMesIssQoSRemarkPortDscpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssQoSRemarkPortDscpEnable.setStatus(_A)
class _EltMesIssQoSRemarkPortDefaultCosSource_Type(EltMesIssQoSRemarkPortDefaultCosSource):defaultValue=1
_EltMesIssQoSRemarkPortDefaultCosSource_Type.__name__=_M
_EltMesIssQoSRemarkPortDefaultCosSource_Object=MibTableColumn
eltMesIssQoSRemarkPortDefaultCosSource=_EltMesIssQoSRemarkPortDefaultCosSource_Object((1,3,6,1,4,1,35265,1,139,5,1,4,1,1,3),_EltMesIssQoSRemarkPortDefaultCosSource_Type())
eltMesIssQoSRemarkPortDefaultCosSource.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssQoSRemarkPortDefaultCosSource.setStatus(_A)
_EltMesIssQoSInterfaces_ObjectIdentity=ObjectIdentity
eltMesIssQoSInterfaces=_EltMesIssQoSInterfaces_ObjectIdentity((1,3,6,1,4,1,35265,1,139,5,1,5))
_EltMesIssQoSIfUtilizationTable_Object=MibTable
eltMesIssQoSIfUtilizationTable=_EltMesIssQoSIfUtilizationTable_Object((1,3,6,1,4,1,35265,1,139,5,1,5,1))
if mibBuilder.loadTexts:eltMesIssQoSIfUtilizationTable.setStatus(_A)
_EltMesIssQoSIfUtilizationEntry_Object=MibTableRow
eltMesIssQoSIfUtilizationEntry=_EltMesIssQoSIfUtilizationEntry_Object((1,3,6,1,4,1,35265,1,139,5,1,5,1,1))
eltMesIssQoSIfUtilizationEntry.setIndexNames((0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:eltMesIssQoSIfUtilizationEntry.setStatus(_A)
_EltMesIssQoSIfUtilizationIfIndex_Type=Integer32
_EltMesIssQoSIfUtilizationIfIndex_Object=MibTableColumn
eltMesIssQoSIfUtilizationIfIndex=_EltMesIssQoSIfUtilizationIfIndex_Object((1,3,6,1,4,1,35265,1,139,5,1,5,1,1,1),_EltMesIssQoSIfUtilizationIfIndex_Type())
eltMesIssQoSIfUtilizationIfIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:eltMesIssQoSIfUtilizationIfIndex.setStatus(_A)
_EltMesIssQoSIfUtilizationInterval_Type=Integer32
_EltMesIssQoSIfUtilizationInterval_Object=MibTableColumn
eltMesIssQoSIfUtilizationInterval=_EltMesIssQoSIfUtilizationInterval_Object((1,3,6,1,4,1,35265,1,139,5,1,5,1,1,2),_EltMesIssQoSIfUtilizationInterval_Type())
eltMesIssQoSIfUtilizationInterval.setMaxAccess(_P)
if mibBuilder.loadTexts:eltMesIssQoSIfUtilizationInterval.setStatus(_A)
_EltMesIssQoSIfUtilizationInPkts_Type=Counter32
_EltMesIssQoSIfUtilizationInPkts_Object=MibTableColumn
eltMesIssQoSIfUtilizationInPkts=_EltMesIssQoSIfUtilizationInPkts_Object((1,3,6,1,4,1,35265,1,139,5,1,5,1,1,3),_EltMesIssQoSIfUtilizationInPkts_Type())
eltMesIssQoSIfUtilizationInPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:eltMesIssQoSIfUtilizationInPkts.setStatus(_A)
_EltMesIssQoSIfUtilizationInRate_Type=Counter32
_EltMesIssQoSIfUtilizationInRate_Object=MibTableColumn
eltMesIssQoSIfUtilizationInRate=_EltMesIssQoSIfUtilizationInRate_Object((1,3,6,1,4,1,35265,1,139,5,1,5,1,1,4),_EltMesIssQoSIfUtilizationInRate_Type())
eltMesIssQoSIfUtilizationInRate.setMaxAccess(_E)
if mibBuilder.loadTexts:eltMesIssQoSIfUtilizationInRate.setStatus(_A)
_EltMesIssQoSIfUtilizationOutPkts_Type=Counter32
_EltMesIssQoSIfUtilizationOutPkts_Object=MibTableColumn
eltMesIssQoSIfUtilizationOutPkts=_EltMesIssQoSIfUtilizationOutPkts_Object((1,3,6,1,4,1,35265,1,139,5,1,5,1,1,5),_EltMesIssQoSIfUtilizationOutPkts_Type())
eltMesIssQoSIfUtilizationOutPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:eltMesIssQoSIfUtilizationOutPkts.setStatus(_A)
_EltMesIssQoSIfUtilizationOutRate_Type=Counter32
_EltMesIssQoSIfUtilizationOutRate_Object=MibTableColumn
eltMesIssQoSIfUtilizationOutRate=_EltMesIssQoSIfUtilizationOutRate_Object((1,3,6,1,4,1,35265,1,139,5,1,5,1,1,6),_EltMesIssQoSIfUtilizationOutRate_Type())
eltMesIssQoSIfUtilizationOutRate.setMaxAccess(_E)
if mibBuilder.loadTexts:eltMesIssQoSIfUtilizationOutRate.setStatus(_A)
_EltMesIssQoSCpuRateControl_ObjectIdentity=ObjectIdentity
eltMesIssQoSCpuRateControl=_EltMesIssQoSCpuRateControl_ObjectIdentity((1,3,6,1,4,1,35265,1,139,5,1,6))
_EltMesIssQoSCpuRateLimitTable_Object=MibTable
eltMesIssQoSCpuRateLimitTable=_EltMesIssQoSCpuRateLimitTable_Object((1,3,6,1,4,1,35265,1,139,5,1,6,1))
if mibBuilder.loadTexts:eltMesIssQoSCpuRateLimitTable.setStatus(_A)
_EltMesIssQoSCpuRateLimitEntry_Object=MibTableRow
eltMesIssQoSCpuRateLimitEntry=_EltMesIssQoSCpuRateLimitEntry_Object((1,3,6,1,4,1,35265,1,139,5,1,6,1,1))
if mibBuilder.loadTexts:eltMesIssQoSCpuRateLimitEntry.setStatus(_A)
class _EltMesIssQoSCpuRateLimitLoggingEnable_Type(TruthValue):defaultValue=2
_EltMesIssQoSCpuRateLimitLoggingEnable_Type.__name__=_C
_EltMesIssQoSCpuRateLimitLoggingEnable_Object=MibTableColumn
eltMesIssQoSCpuRateLimitLoggingEnable=_EltMesIssQoSCpuRateLimitLoggingEnable_Object((1,3,6,1,4,1,35265,1,139,5,1,6,1,1,1),_EltMesIssQoSCpuRateLimitLoggingEnable_Type())
eltMesIssQoSCpuRateLimitLoggingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssQoSCpuRateLimitLoggingEnable.setStatus(_A)
class _EltMesIssQoSCpuRateLimitTrapEnable_Type(TruthValue):defaultValue=2
_EltMesIssQoSCpuRateLimitTrapEnable_Type.__name__=_C
_EltMesIssQoSCpuRateLimitTrapEnable_Object=MibTableColumn
eltMesIssQoSCpuRateLimitTrapEnable=_EltMesIssQoSCpuRateLimitTrapEnable_Object((1,3,6,1,4,1,35265,1,139,5,1,6,1,1,2),_EltMesIssQoSCpuRateLimitTrapEnable_Type())
eltMesIssQoSCpuRateLimitTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssQoSCpuRateLimitTrapEnable.setStatus(_A)
_EltMesIssQoSNotifications_ObjectIdentity=ObjectIdentity
eltMesIssQoSNotifications=_EltMesIssQoSNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,139,5,2))
_EltMesIssQoSNotificationsPrefix_ObjectIdentity=ObjectIdentity
eltMesIssQoSNotificationsPrefix=_EltMesIssQoSNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,35265,1,139,5,2,0))
fsQoSMeterEntry.registerAugmentions((_D,_Q))
eltMesIssQoSMeterEntry.setIndexNames(*fsQoSMeterEntry.getIndexNames())
fsQosHwCpuRateLimitEntry.registerAugmentions((_D,_R))
eltMesIssQoSCpuRateLimitEntry.setIndexNames(*fsQosHwCpuRateLimitEntry.getIndexNames())
eltMesIssQoSCpuRateLimitTrap=NotificationType((1,3,6,1,4,1,35265,1,139,5,2,0,1))
eltMesIssQoSCpuRateLimitTrap.setObjects(*((_F,_J),(_F,_I)))
if mibBuilder.loadTexts:eltMesIssQoSCpuRateLimitTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_L:EltMesIssQoSTrustMode,_K:EltMesIssMeterUnits,_M:EltMesIssQoSRemarkPortDefaultCosSource,'eltMesIssQoSMIB':eltMesIssQoSMIB,'eltMesIssQoSObjects':eltMesIssQoSObjects,'eltMesIssQoSGlobals':eltMesIssQoSGlobals,'eltMesIssQoSTrustMode':eltMesIssQoSTrustMode,'eltMesIssQoSMetering':eltMesIssQoSMetering,'eltMesIssQoSMeterTable':eltMesIssQoSMeterTable,_Q:eltMesIssQoSMeterEntry,'eltMesIssQoSMeterUnits':eltMesIssQoSMeterUnits,'eltMesIssQoSTrafficMgmt':eltMesIssQoSTrafficMgmt,'eltMesIssQoSPortTrustModeTable':eltMesIssQoSPortTrustModeTable,'eltMesIssQoSPortTrustModeEntry':eltMesIssQoSPortTrustModeEntry,'eltMesIssQoSPortTrustMode':eltMesIssQoSPortTrustMode,'eltMesIssQoSRemarking':eltMesIssQoSRemarking,'eltMesIssQoSRemarkPortTable':eltMesIssQoSRemarkPortTable,'eltMesIssQoSRemarkPortEntry':eltMesIssQoSRemarkPortEntry,'eltMesIssQoSRemarkPortCosEnable':eltMesIssQoSRemarkPortCosEnable,'eltMesIssQoSRemarkPortDscpEnable':eltMesIssQoSRemarkPortDscpEnable,'eltMesIssQoSRemarkPortDefaultCosSource':eltMesIssQoSRemarkPortDefaultCosSource,'eltMesIssQoSInterfaces':eltMesIssQoSInterfaces,'eltMesIssQoSIfUtilizationTable':eltMesIssQoSIfUtilizationTable,'eltMesIssQoSIfUtilizationEntry':eltMesIssQoSIfUtilizationEntry,_N:eltMesIssQoSIfUtilizationIfIndex,_O:eltMesIssQoSIfUtilizationInterval,'eltMesIssQoSIfUtilizationInPkts':eltMesIssQoSIfUtilizationInPkts,'eltMesIssQoSIfUtilizationInRate':eltMesIssQoSIfUtilizationInRate,'eltMesIssQoSIfUtilizationOutPkts':eltMesIssQoSIfUtilizationOutPkts,'eltMesIssQoSIfUtilizationOutRate':eltMesIssQoSIfUtilizationOutRate,'eltMesIssQoSCpuRateControl':eltMesIssQoSCpuRateControl,'eltMesIssQoSCpuRateLimitTable':eltMesIssQoSCpuRateLimitTable,_R:eltMesIssQoSCpuRateLimitEntry,'eltMesIssQoSCpuRateLimitLoggingEnable':eltMesIssQoSCpuRateLimitLoggingEnable,'eltMesIssQoSCpuRateLimitTrapEnable':eltMesIssQoSCpuRateLimitTrapEnable,'eltMesIssQoSNotifications':eltMesIssQoSNotifications,'eltMesIssQoSNotificationsPrefix':eltMesIssQoSNotificationsPrefix,'eltMesIssQoSCpuRateLimitTrap':eltMesIssQoSCpuRateLimitTrap})