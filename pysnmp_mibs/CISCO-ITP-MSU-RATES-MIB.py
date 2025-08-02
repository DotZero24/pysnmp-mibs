_x='ciscoItpMsuRatesObjectsRev1'
_w='ciscoItpMsuRateState'
_v='cimrMsuTrafficMSUs'
_u='cimrMsuDist090orAbove'
_t='cimrMsuDist080to089Seconds'
_s='cimrMsuDist070to079Seconds'
_r='cimrMsuDist060to069Seconds'
_q='cimrMsuDist050to059Seconds'
_p='cimrMsuDist040to049Seconds'
_o='cimrMsuDist030to039Seconds'
_n='cimrMsuDist020to029Seconds'
_m='cimrMsuDist010to019Seconds'
_l='cimrMsuDist000to009Seconds'
_k='cimrMsuTrafficMaxTimestamp'
_j='cimrMsuTrafficMaxRate'
_i='cimrMsuTrafficDurOverloaded'
_h='cimrMsuTrafficDurWarning'
_g='cimrMsuProcBayNumber'
_f='cimrMsuProcSlotNumber'
_e='cimrMsuProcResetTimestamp'
_d='cimrMsuProcReset'
_c='cimrMsuProcOverloadedThreshold'
_b='cimrMsuProcWarningThreshold'
_a='cimrMsuProcAcceptableThreshold'
_Z='cimrMsuProcPhysicalIndex'
_Y='cimrMsuRateOverloadedThreshold'
_X='cimrMsuRateWarningThreshold'
_W='cimrMsuRateAcceptableThreshold'
_V='cimrMsuRateNotifyEnable'
_U='cimrMsuRateNotifyInterval'
_T='cimrMsuRateSampleInterval'
_S='not-accessible'
_R='TruthValue'
_Q='ciscoItpMsuRatesNotifyGroup'
_P='ciscoItpMsuDistObjects'
_O='ciscoItpMsuRatesObjects'
_N='ciscoItpMsuRatesScalarsGroup'
_M='cimrMsuTrafficSize'
_L='cimrMsuTrafficRate'
_K='cimrMsuTrafficRateState'
_J='cimrMsuTrafficDirection'
_I='cimrMsuProcIndex'
_H='Unsigned32'
_G='MSUs per second'
_F='CimrMsuThreshold'
_E='read-write'
_D='seconds'
_C='read-only'
_B='CISCO-ITP-MSU-RATES-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
EntPhysicalIndexOrZero,=mibBuilder.importSymbols('CISCO-TC','EntPhysicalIndexOrZero')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_R)
ciscoItpMsuRatesMIB=ModuleIdentity((1,3,6,1,4,1,9,9,529))
if mibBuilder.loadTexts:ciscoItpMsuRatesMIB.setRevisions(('2007-02-01 00:00','2006-05-31 00:00'))
class CimrMsuThreshold(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(100,4294967295))
class CimrMsuRateState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('acceptable',1),('warning',2),('overloaded',3)))
class CirbhMsuTrafficDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('receive',1),('transmit',2)))
class CirbhMsuCurrentCount(TextualConvention,Gauge32):status=_A
_CiscoItpMsuRatesMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoItpMsuRatesMIBNotifs=_CiscoItpMsuRatesMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,529,0))
_CiscoItpMsuRatesMIBObjects_ObjectIdentity=ObjectIdentity
ciscoItpMsuRatesMIBObjects=_CiscoItpMsuRatesMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,529,1))
_CimrScalars_ObjectIdentity=ObjectIdentity
cimrScalars=_CimrScalars_ObjectIdentity((1,3,6,1,4,1,9,9,529,1,1))
class _CimrMsuRateSampleInterval_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_CimrMsuRateSampleInterval_Type.__name__=_H
_CimrMsuRateSampleInterval_Object=MibScalar
cimrMsuRateSampleInterval=_CimrMsuRateSampleInterval_Object((1,3,6,1,4,1,9,9,529,1,1,4),_CimrMsuRateSampleInterval_Type())
cimrMsuRateSampleInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cimrMsuRateSampleInterval.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuRateSampleInterval.setUnits(_D)
class _CimrMsuRateNotifyInterval_Type(Unsigned32):defaultValue=900;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(60,3600))
_CimrMsuRateNotifyInterval_Type.__name__=_H
_CimrMsuRateNotifyInterval_Object=MibScalar
cimrMsuRateNotifyInterval=_CimrMsuRateNotifyInterval_Object((1,3,6,1,4,1,9,9,529,1,1,5),_CimrMsuRateNotifyInterval_Type())
cimrMsuRateNotifyInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cimrMsuRateNotifyInterval.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuRateNotifyInterval.setUnits(_D)
class _CimrMsuRateNotifyEnable_Type(TruthValue):defaultValue=2
_CimrMsuRateNotifyEnable_Type.__name__=_R
_CimrMsuRateNotifyEnable_Object=MibScalar
cimrMsuRateNotifyEnable=_CimrMsuRateNotifyEnable_Object((1,3,6,1,4,1,9,9,529,1,1,6),_CimrMsuRateNotifyEnable_Type())
cimrMsuRateNotifyEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cimrMsuRateNotifyEnable.setStatus(_A)
class _CimrMsuRateAcceptableThreshold_Type(CimrMsuThreshold):defaultValue=0
_CimrMsuRateAcceptableThreshold_Type.__name__=_F
_CimrMsuRateAcceptableThreshold_Object=MibScalar
cimrMsuRateAcceptableThreshold=_CimrMsuRateAcceptableThreshold_Object((1,3,6,1,4,1,9,9,529,1,1,7),_CimrMsuRateAcceptableThreshold_Type())
cimrMsuRateAcceptableThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cimrMsuRateAcceptableThreshold.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuRateAcceptableThreshold.setUnits(_G)
class _CimrMsuRateWarningThreshold_Type(CimrMsuThreshold):defaultValue=0
_CimrMsuRateWarningThreshold_Type.__name__=_F
_CimrMsuRateWarningThreshold_Object=MibScalar
cimrMsuRateWarningThreshold=_CimrMsuRateWarningThreshold_Object((1,3,6,1,4,1,9,9,529,1,1,8),_CimrMsuRateWarningThreshold_Type())
cimrMsuRateWarningThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cimrMsuRateWarningThreshold.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuRateWarningThreshold.setUnits(_G)
class _CimrMsuRateOverloadedThreshold_Type(CimrMsuThreshold):defaultValue=0
_CimrMsuRateOverloadedThreshold_Type.__name__=_F
_CimrMsuRateOverloadedThreshold_Object=MibScalar
cimrMsuRateOverloadedThreshold=_CimrMsuRateOverloadedThreshold_Object((1,3,6,1,4,1,9,9,529,1,1,9),_CimrMsuRateOverloadedThreshold_Type())
cimrMsuRateOverloadedThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cimrMsuRateOverloadedThreshold.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuRateOverloadedThreshold.setUnits(_G)
_CimrTables_ObjectIdentity=ObjectIdentity
cimrTables=_CimrTables_ObjectIdentity((1,3,6,1,4,1,9,9,529,1,2))
_CimrMsuProcTable_Object=MibTable
cimrMsuProcTable=_CimrMsuProcTable_Object((1,3,6,1,4,1,9,9,529,1,2,1))
if mibBuilder.loadTexts:cimrMsuProcTable.setStatus(_A)
_CimrMsuProcEntry_Object=MibTableRow
cimrMsuProcEntry=_CimrMsuProcEntry_Object((1,3,6,1,4,1,9,9,529,1,2,1,1))
cimrMsuProcEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:cimrMsuProcEntry.setStatus(_A)
class _CimrMsuProcIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CimrMsuProcIndex_Type.__name__=_H
_CimrMsuProcIndex_Object=MibTableColumn
cimrMsuProcIndex=_CimrMsuProcIndex_Object((1,3,6,1,4,1,9,9,529,1,2,1,1,1),_CimrMsuProcIndex_Type())
cimrMsuProcIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:cimrMsuProcIndex.setStatus(_A)
_CimrMsuProcPhysicalIndex_Type=EntPhysicalIndexOrZero
_CimrMsuProcPhysicalIndex_Object=MibTableColumn
cimrMsuProcPhysicalIndex=_CimrMsuProcPhysicalIndex_Object((1,3,6,1,4,1,9,9,529,1,2,1,1,2),_CimrMsuProcPhysicalIndex_Type())
cimrMsuProcPhysicalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuProcPhysicalIndex.setStatus(_A)
class _CimrMsuProcAcceptableThreshold_Type(CimrMsuThreshold):defaultValue=0
_CimrMsuProcAcceptableThreshold_Type.__name__=_F
_CimrMsuProcAcceptableThreshold_Object=MibTableColumn
cimrMsuProcAcceptableThreshold=_CimrMsuProcAcceptableThreshold_Object((1,3,6,1,4,1,9,9,529,1,2,1,1,3),_CimrMsuProcAcceptableThreshold_Type())
cimrMsuProcAcceptableThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cimrMsuProcAcceptableThreshold.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuProcAcceptableThreshold.setUnits(_G)
class _CimrMsuProcWarningThreshold_Type(CimrMsuThreshold):defaultValue=0
_CimrMsuProcWarningThreshold_Type.__name__=_F
_CimrMsuProcWarningThreshold_Object=MibTableColumn
cimrMsuProcWarningThreshold=_CimrMsuProcWarningThreshold_Object((1,3,6,1,4,1,9,9,529,1,2,1,1,4),_CimrMsuProcWarningThreshold_Type())
cimrMsuProcWarningThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cimrMsuProcWarningThreshold.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuProcWarningThreshold.setUnits(_G)
class _CimrMsuProcOverloadedThreshold_Type(CimrMsuThreshold):defaultValue=0
_CimrMsuProcOverloadedThreshold_Type.__name__=_F
_CimrMsuProcOverloadedThreshold_Object=MibTableColumn
cimrMsuProcOverloadedThreshold=_CimrMsuProcOverloadedThreshold_Object((1,3,6,1,4,1,9,9,529,1,2,1,1,5),_CimrMsuProcOverloadedThreshold_Type())
cimrMsuProcOverloadedThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cimrMsuProcOverloadedThreshold.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuProcOverloadedThreshold.setUnits(_G)
_CimrMsuProcReset_Type=TruthValue
_CimrMsuProcReset_Object=MibTableColumn
cimrMsuProcReset=_CimrMsuProcReset_Object((1,3,6,1,4,1,9,9,529,1,2,1,1,6),_CimrMsuProcReset_Type())
cimrMsuProcReset.setMaxAccess(_E)
if mibBuilder.loadTexts:cimrMsuProcReset.setStatus(_A)
_CimrMsuProcResetTimestamp_Type=TimeStamp
_CimrMsuProcResetTimestamp_Object=MibTableColumn
cimrMsuProcResetTimestamp=_CimrMsuProcResetTimestamp_Object((1,3,6,1,4,1,9,9,529,1,2,1,1,7),_CimrMsuProcResetTimestamp_Type())
cimrMsuProcResetTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuProcResetTimestamp.setStatus(_A)
_CimrMsuProcSlotNumber_Type=Integer32
_CimrMsuProcSlotNumber_Object=MibTableColumn
cimrMsuProcSlotNumber=_CimrMsuProcSlotNumber_Object((1,3,6,1,4,1,9,9,529,1,2,1,1,8),_CimrMsuProcSlotNumber_Type())
cimrMsuProcSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuProcSlotNumber.setStatus(_A)
_CimrMsuProcBayNumber_Type=Integer32
_CimrMsuProcBayNumber_Object=MibTableColumn
cimrMsuProcBayNumber=_CimrMsuProcBayNumber_Object((1,3,6,1,4,1,9,9,529,1,2,1,1,9),_CimrMsuProcBayNumber_Type())
cimrMsuProcBayNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuProcBayNumber.setStatus(_A)
_CimrMsuTrafficTable_Object=MibTable
cimrMsuTrafficTable=_CimrMsuTrafficTable_Object((1,3,6,1,4,1,9,9,529,1,2,2))
if mibBuilder.loadTexts:cimrMsuTrafficTable.setStatus(_A)
_CimrMsuTrafficEntry_Object=MibTableRow
cimrMsuTrafficEntry=_CimrMsuTrafficEntry_Object((1,3,6,1,4,1,9,9,529,1,2,2,1))
cimrMsuTrafficEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:cimrMsuTrafficEntry.setStatus(_A)
_CimrMsuTrafficDirection_Type=CirbhMsuTrafficDirection
_CimrMsuTrafficDirection_Object=MibTableColumn
cimrMsuTrafficDirection=_CimrMsuTrafficDirection_Object((1,3,6,1,4,1,9,9,529,1,2,2,1,1),_CimrMsuTrafficDirection_Type())
cimrMsuTrafficDirection.setMaxAccess(_S)
if mibBuilder.loadTexts:cimrMsuTrafficDirection.setStatus(_A)
_CimrMsuTrafficRateState_Type=CimrMsuRateState
_CimrMsuTrafficRateState_Object=MibTableColumn
cimrMsuTrafficRateState=_CimrMsuTrafficRateState_Object((1,3,6,1,4,1,9,9,529,1,2,2,1,2),_CimrMsuTrafficRateState_Type())
cimrMsuTrafficRateState.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuTrafficRateState.setStatus(_A)
_CimrMsuTrafficRate_Type=Gauge32
_CimrMsuTrafficRate_Object=MibTableColumn
cimrMsuTrafficRate=_CimrMsuTrafficRate_Object((1,3,6,1,4,1,9,9,529,1,2,2,1,3),_CimrMsuTrafficRate_Type())
cimrMsuTrafficRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuTrafficRate.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuTrafficRate.setUnits('MSUs per seconds')
_CimrMsuTrafficSize_Type=Gauge32
_CimrMsuTrafficSize_Object=MibTableColumn
cimrMsuTrafficSize=_CimrMsuTrafficSize_Object((1,3,6,1,4,1,9,9,529,1,2,2,1,4),_CimrMsuTrafficSize_Type())
cimrMsuTrafficSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuTrafficSize.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuTrafficSize.setUnits('Average bytes per MSU')
_CimrMsuTrafficDurWarning_Type=CirbhMsuCurrentCount
_CimrMsuTrafficDurWarning_Object=MibTableColumn
cimrMsuTrafficDurWarning=_CimrMsuTrafficDurWarning_Object((1,3,6,1,4,1,9,9,529,1,2,2,1,5),_CimrMsuTrafficDurWarning_Type())
cimrMsuTrafficDurWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuTrafficDurWarning.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuTrafficDurWarning.setUnits(_D)
_CimrMsuTrafficDurOverloaded_Type=CirbhMsuCurrentCount
_CimrMsuTrafficDurOverloaded_Object=MibTableColumn
cimrMsuTrafficDurOverloaded=_CimrMsuTrafficDurOverloaded_Object((1,3,6,1,4,1,9,9,529,1,2,2,1,6),_CimrMsuTrafficDurOverloaded_Type())
cimrMsuTrafficDurOverloaded.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuTrafficDurOverloaded.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuTrafficDurOverloaded.setUnits(_D)
_CimrMsuTrafficMaxRate_Type=Gauge32
_CimrMsuTrafficMaxRate_Object=MibTableColumn
cimrMsuTrafficMaxRate=_CimrMsuTrafficMaxRate_Object((1,3,6,1,4,1,9,9,529,1,2,2,1,7),_CimrMsuTrafficMaxRate_Type())
cimrMsuTrafficMaxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuTrafficMaxRate.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuTrafficMaxRate.setUnits(_G)
_CimrMsuTrafficMaxTimestamp_Type=TimeStamp
_CimrMsuTrafficMaxTimestamp_Object=MibTableColumn
cimrMsuTrafficMaxTimestamp=_CimrMsuTrafficMaxTimestamp_Object((1,3,6,1,4,1,9,9,529,1,2,2,1,8),_CimrMsuTrafficMaxTimestamp_Type())
cimrMsuTrafficMaxTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuTrafficMaxTimestamp.setStatus(_A)
_CimrMsuTrafficMSUs_Type=Counter32
_CimrMsuTrafficMSUs_Object=MibTableColumn
cimrMsuTrafficMSUs=_CimrMsuTrafficMSUs_Object((1,3,6,1,4,1,9,9,529,1,2,2,1,9),_CimrMsuTrafficMSUs_Type())
cimrMsuTrafficMSUs.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuTrafficMSUs.setStatus(_A)
_CimrMsuDistTable_Object=MibTable
cimrMsuDistTable=_CimrMsuDistTable_Object((1,3,6,1,4,1,9,9,529,1,2,3))
if mibBuilder.loadTexts:cimrMsuDistTable.setStatus(_A)
_CimrMsuDistEntry_Object=MibTableRow
cimrMsuDistEntry=_CimrMsuDistEntry_Object((1,3,6,1,4,1,9,9,529,1,2,3,1))
cimrMsuDistEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:cimrMsuDistEntry.setStatus(_A)
_CimrMsuDist000to009Seconds_Type=CirbhMsuCurrentCount
_CimrMsuDist000to009Seconds_Object=MibTableColumn
cimrMsuDist000to009Seconds=_CimrMsuDist000to009Seconds_Object((1,3,6,1,4,1,9,9,529,1,2,3,1,1),_CimrMsuDist000to009Seconds_Type())
cimrMsuDist000to009Seconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuDist000to009Seconds.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuDist000to009Seconds.setUnits(_D)
_CimrMsuDist010to019Seconds_Type=CirbhMsuCurrentCount
_CimrMsuDist010to019Seconds_Object=MibTableColumn
cimrMsuDist010to019Seconds=_CimrMsuDist010to019Seconds_Object((1,3,6,1,4,1,9,9,529,1,2,3,1,2),_CimrMsuDist010to019Seconds_Type())
cimrMsuDist010to019Seconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuDist010to019Seconds.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuDist010to019Seconds.setUnits(_D)
_CimrMsuDist020to029Seconds_Type=CirbhMsuCurrentCount
_CimrMsuDist020to029Seconds_Object=MibTableColumn
cimrMsuDist020to029Seconds=_CimrMsuDist020to029Seconds_Object((1,3,6,1,4,1,9,9,529,1,2,3,1,3),_CimrMsuDist020to029Seconds_Type())
cimrMsuDist020to029Seconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuDist020to029Seconds.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuDist020to029Seconds.setUnits(_D)
_CimrMsuDist030to039Seconds_Type=CirbhMsuCurrentCount
_CimrMsuDist030to039Seconds_Object=MibTableColumn
cimrMsuDist030to039Seconds=_CimrMsuDist030to039Seconds_Object((1,3,6,1,4,1,9,9,529,1,2,3,1,4),_CimrMsuDist030to039Seconds_Type())
cimrMsuDist030to039Seconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuDist030to039Seconds.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuDist030to039Seconds.setUnits(_D)
_CimrMsuDist040to049Seconds_Type=CirbhMsuCurrentCount
_CimrMsuDist040to049Seconds_Object=MibTableColumn
cimrMsuDist040to049Seconds=_CimrMsuDist040to049Seconds_Object((1,3,6,1,4,1,9,9,529,1,2,3,1,5),_CimrMsuDist040to049Seconds_Type())
cimrMsuDist040to049Seconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuDist040to049Seconds.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuDist040to049Seconds.setUnits(_D)
_CimrMsuDist050to059Seconds_Type=CirbhMsuCurrentCount
_CimrMsuDist050to059Seconds_Object=MibTableColumn
cimrMsuDist050to059Seconds=_CimrMsuDist050to059Seconds_Object((1,3,6,1,4,1,9,9,529,1,2,3,1,6),_CimrMsuDist050to059Seconds_Type())
cimrMsuDist050to059Seconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuDist050to059Seconds.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuDist050to059Seconds.setUnits(_D)
_CimrMsuDist060to069Seconds_Type=CirbhMsuCurrentCount
_CimrMsuDist060to069Seconds_Object=MibTableColumn
cimrMsuDist060to069Seconds=_CimrMsuDist060to069Seconds_Object((1,3,6,1,4,1,9,9,529,1,2,3,1,7),_CimrMsuDist060to069Seconds_Type())
cimrMsuDist060to069Seconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuDist060to069Seconds.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuDist060to069Seconds.setUnits(_D)
_CimrMsuDist070to079Seconds_Type=CirbhMsuCurrentCount
_CimrMsuDist070to079Seconds_Object=MibTableColumn
cimrMsuDist070to079Seconds=_CimrMsuDist070to079Seconds_Object((1,3,6,1,4,1,9,9,529,1,2,3,1,8),_CimrMsuDist070to079Seconds_Type())
cimrMsuDist070to079Seconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuDist070to079Seconds.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuDist070to079Seconds.setUnits(_D)
_CimrMsuDist080to089Seconds_Type=CirbhMsuCurrentCount
_CimrMsuDist080to089Seconds_Object=MibTableColumn
cimrMsuDist080to089Seconds=_CimrMsuDist080to089Seconds_Object((1,3,6,1,4,1,9,9,529,1,2,3,1,9),_CimrMsuDist080to089Seconds_Type())
cimrMsuDist080to089Seconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuDist080to089Seconds.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuDist080to089Seconds.setUnits(_D)
_CimrMsuDist090orAbove_Type=CirbhMsuCurrentCount
_CimrMsuDist090orAbove_Object=MibTableColumn
cimrMsuDist090orAbove=_CimrMsuDist090orAbove_Object((1,3,6,1,4,1,9,9,529,1,2,3,1,10),_CimrMsuDist090orAbove_Type())
cimrMsuDist090orAbove.setMaxAccess(_C)
if mibBuilder.loadTexts:cimrMsuDist090orAbove.setStatus(_A)
if mibBuilder.loadTexts:cimrMsuDist090orAbove.setUnits(_D)
_CiscoItpMsuRatesMIBConform_ObjectIdentity=ObjectIdentity
ciscoItpMsuRatesMIBConform=_CiscoItpMsuRatesMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,529,2))
_CiscoItpMsuRatesMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoItpMsuRatesMIBCompliances=_CiscoItpMsuRatesMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,529,2,1))
_CiscoItpMsuRatesMIBGroups_ObjectIdentity=ObjectIdentity
ciscoItpMsuRatesMIBGroups=_CiscoItpMsuRatesMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,529,2,2))
ciscoItpMsuRatesScalarsGroup=ObjectGroup((1,3,6,1,4,1,9,9,529,2,2,1))
ciscoItpMsuRatesScalarsGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:ciscoItpMsuRatesScalarsGroup.setStatus(_A)
ciscoItpMsuRatesObjects=ObjectGroup((1,3,6,1,4,1,9,9,529,2,2,2))
ciscoItpMsuRatesObjects.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_K),(_B,_L),(_B,_M),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:ciscoItpMsuRatesObjects.setStatus(_A)
ciscoItpMsuDistObjects=ObjectGroup((1,3,6,1,4,1,9,9,529,2,2,3))
ciscoItpMsuDistObjects.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:ciscoItpMsuDistObjects.setStatus(_A)
ciscoItpMsuRatesObjectsRev1=ObjectGroup((1,3,6,1,4,1,9,9,529,2,2,5))
ciscoItpMsuRatesObjectsRev1.setObjects((_B,_v))
if mibBuilder.loadTexts:ciscoItpMsuRatesObjectsRev1.setStatus(_A)
ciscoItpMsuRateState=NotificationType((1,3,6,1,4,1,9,9,529,0,1))
ciscoItpMsuRateState.setObjects(*((_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ciscoItpMsuRateState.setStatus(_A)
ciscoItpMsuRatesNotifyGroup=NotificationGroup((1,3,6,1,4,1,9,9,529,2,2,4))
ciscoItpMsuRatesNotifyGroup.setObjects((_B,_w))
if mibBuilder.loadTexts:ciscoItpMsuRatesNotifyGroup.setStatus(_A)
ciscoItpMsuRatesMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,529,2,1,1))
ciscoItpMsuRatesMIBCompliance.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ciscoItpMsuRatesMIBCompliance.setStatus('deprecated')
ciscoItpMsuRatesMIBCompliancesRev1=ModuleCompliance((1,3,6,1,4,1,9,9,529,2,1,2))
ciscoItpMsuRatesMIBCompliancesRev1.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_x)))
if mibBuilder.loadTexts:ciscoItpMsuRatesMIBCompliancesRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_F:CimrMsuThreshold,'CimrMsuRateState':CimrMsuRateState,'CirbhMsuTrafficDirection':CirbhMsuTrafficDirection,'CirbhMsuCurrentCount':CirbhMsuCurrentCount,'ciscoItpMsuRatesMIB':ciscoItpMsuRatesMIB,'ciscoItpMsuRatesMIBNotifs':ciscoItpMsuRatesMIBNotifs,_w:ciscoItpMsuRateState,'ciscoItpMsuRatesMIBObjects':ciscoItpMsuRatesMIBObjects,'cimrScalars':cimrScalars,_T:cimrMsuRateSampleInterval,_U:cimrMsuRateNotifyInterval,_V:cimrMsuRateNotifyEnable,_W:cimrMsuRateAcceptableThreshold,_X:cimrMsuRateWarningThreshold,_Y:cimrMsuRateOverloadedThreshold,'cimrTables':cimrTables,'cimrMsuProcTable':cimrMsuProcTable,'cimrMsuProcEntry':cimrMsuProcEntry,_I:cimrMsuProcIndex,_Z:cimrMsuProcPhysicalIndex,_a:cimrMsuProcAcceptableThreshold,_b:cimrMsuProcWarningThreshold,_c:cimrMsuProcOverloadedThreshold,_d:cimrMsuProcReset,_e:cimrMsuProcResetTimestamp,_f:cimrMsuProcSlotNumber,_g:cimrMsuProcBayNumber,'cimrMsuTrafficTable':cimrMsuTrafficTable,'cimrMsuTrafficEntry':cimrMsuTrafficEntry,_J:cimrMsuTrafficDirection,_K:cimrMsuTrafficRateState,_L:cimrMsuTrafficRate,_M:cimrMsuTrafficSize,_h:cimrMsuTrafficDurWarning,_i:cimrMsuTrafficDurOverloaded,_j:cimrMsuTrafficMaxRate,_k:cimrMsuTrafficMaxTimestamp,_v:cimrMsuTrafficMSUs,'cimrMsuDistTable':cimrMsuDistTable,'cimrMsuDistEntry':cimrMsuDistEntry,_l:cimrMsuDist000to009Seconds,_m:cimrMsuDist010to019Seconds,_n:cimrMsuDist020to029Seconds,_o:cimrMsuDist030to039Seconds,_p:cimrMsuDist040to049Seconds,_q:cimrMsuDist050to059Seconds,_r:cimrMsuDist060to069Seconds,_s:cimrMsuDist070to079Seconds,_t:cimrMsuDist080to089Seconds,_u:cimrMsuDist090orAbove,'ciscoItpMsuRatesMIBConform':ciscoItpMsuRatesMIBConform,'ciscoItpMsuRatesMIBCompliances':ciscoItpMsuRatesMIBCompliances,'ciscoItpMsuRatesMIBCompliance':ciscoItpMsuRatesMIBCompliance,'ciscoItpMsuRatesMIBCompliancesRev1':ciscoItpMsuRatesMIBCompliancesRev1,'ciscoItpMsuRatesMIBGroups':ciscoItpMsuRatesMIBGroups,_N:ciscoItpMsuRatesScalarsGroup,_O:ciscoItpMsuRatesObjects,_P:ciscoItpMsuDistObjects,_Q:ciscoItpMsuRatesNotifyGroup,_x:ciscoItpMsuRatesObjectsRev1})