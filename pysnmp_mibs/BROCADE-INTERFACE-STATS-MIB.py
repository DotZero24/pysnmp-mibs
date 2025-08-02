_W='bcsiIfWatermarkGroup'
_V='bcsiIfStatsGroup'
_U='bcsiIfWatermarkWindowStartTime'
_T='bcsiIfWatermarkUpdateTime'
_S='bcsiIfWatermarkPktRate'
_R='bcsiIfWatermarkBitRate'
_Q='bcsiIfStatsInJumboFrames'
_P='bcsiIfStatsOutUtilization'
_O='bcsiIfStatsInUtilization'
_N='bcsiIfStatsOutPktsPerSec'
_M='bcsiIfStatsInPktsPerSec'
_L='bcsiIfStatsOutBitsPerSec'
_K='bcsiIfStatsInBitsPerSec'
_J='bcsiIfWatermarkType'
_I='bcsiIfWatermarkTrafficDirection'
_H='bcsiIfWatermarkWindowType'
_G='not-accessible'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='BROCADE-INTERFACE-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bcsiModules,=mibBuilder.importSymbols('Brocade-REG-MIB','bcsiModules')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
brocadeInterfaceStatsMIB=ModuleIdentity((1,3,6,1,4,1,1588,3,1,11))
if mibBuilder.loadTexts:brocadeInterfaceStatsMIB.setRevisions(('2018-05-29 12:00','2016-09-30 00:00'))
_BcsiIfStatsNotifications_ObjectIdentity=ObjectIdentity
bcsiIfStatsNotifications=_BcsiIfStatsNotifications_ObjectIdentity((1,3,6,1,4,1,1588,3,1,11,0))
_BcsiIfStatsObjects_ObjectIdentity=ObjectIdentity
bcsiIfStatsObjects=_BcsiIfStatsObjects_ObjectIdentity((1,3,6,1,4,1,1588,3,1,11,1))
_BcsiIfStatsTable_Object=MibTable
bcsiIfStatsTable=_BcsiIfStatsTable_Object((1,3,6,1,4,1,1588,3,1,11,1,1))
if mibBuilder.loadTexts:bcsiIfStatsTable.setStatus(_A)
_BcsiIfStatsEntry_Object=MibTableRow
bcsiIfStatsEntry=_BcsiIfStatsEntry_Object((1,3,6,1,4,1,1588,3,1,11,1,1,1))
bcsiIfStatsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:bcsiIfStatsEntry.setStatus(_A)
_BcsiIfStatsInBitsPerSec_Type=CounterBasedGauge64
_BcsiIfStatsInBitsPerSec_Object=MibTableColumn
bcsiIfStatsInBitsPerSec=_BcsiIfStatsInBitsPerSec_Object((1,3,6,1,4,1,1588,3,1,11,1,1,1,1),_BcsiIfStatsInBitsPerSec_Type())
bcsiIfStatsInBitsPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiIfStatsInBitsPerSec.setStatus(_A)
_BcsiIfStatsOutBitsPerSec_Type=CounterBasedGauge64
_BcsiIfStatsOutBitsPerSec_Object=MibTableColumn
bcsiIfStatsOutBitsPerSec=_BcsiIfStatsOutBitsPerSec_Object((1,3,6,1,4,1,1588,3,1,11,1,1,1,2),_BcsiIfStatsOutBitsPerSec_Type())
bcsiIfStatsOutBitsPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiIfStatsOutBitsPerSec.setStatus(_A)
_BcsiIfStatsInPktsPerSec_Type=Gauge32
_BcsiIfStatsInPktsPerSec_Object=MibTableColumn
bcsiIfStatsInPktsPerSec=_BcsiIfStatsInPktsPerSec_Object((1,3,6,1,4,1,1588,3,1,11,1,1,1,3),_BcsiIfStatsInPktsPerSec_Type())
bcsiIfStatsInPktsPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiIfStatsInPktsPerSec.setStatus(_A)
_BcsiIfStatsOutPktsPerSec_Type=Gauge32
_BcsiIfStatsOutPktsPerSec_Object=MibTableColumn
bcsiIfStatsOutPktsPerSec=_BcsiIfStatsOutPktsPerSec_Object((1,3,6,1,4,1,1588,3,1,11,1,1,1,4),_BcsiIfStatsOutPktsPerSec_Type())
bcsiIfStatsOutPktsPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiIfStatsOutPktsPerSec.setStatus(_A)
_BcsiIfStatsInUtilization_Type=Unsigned32
_BcsiIfStatsInUtilization_Object=MibTableColumn
bcsiIfStatsInUtilization=_BcsiIfStatsInUtilization_Object((1,3,6,1,4,1,1588,3,1,11,1,1,1,5),_BcsiIfStatsInUtilization_Type())
bcsiIfStatsInUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiIfStatsInUtilization.setStatus(_A)
_BcsiIfStatsOutUtilization_Type=Unsigned32
_BcsiIfStatsOutUtilization_Object=MibTableColumn
bcsiIfStatsOutUtilization=_BcsiIfStatsOutUtilization_Object((1,3,6,1,4,1,1588,3,1,11,1,1,1,6),_BcsiIfStatsOutUtilization_Type())
bcsiIfStatsOutUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiIfStatsOutUtilization.setStatus(_A)
_BcsiIfStatsInJumboFrames_Type=Counter64
_BcsiIfStatsInJumboFrames_Object=MibTableColumn
bcsiIfStatsInJumboFrames=_BcsiIfStatsInJumboFrames_Object((1,3,6,1,4,1,1588,3,1,11,1,1,1,7),_BcsiIfStatsInJumboFrames_Type())
bcsiIfStatsInJumboFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiIfStatsInJumboFrames.setStatus(_A)
_BcsiIfWatermarkTable_Object=MibTable
bcsiIfWatermarkTable=_BcsiIfWatermarkTable_Object((1,3,6,1,4,1,1588,3,1,11,1,2))
if mibBuilder.loadTexts:bcsiIfWatermarkTable.setStatus(_A)
_BcsiIfWatermarkEntry_Object=MibTableRow
bcsiIfWatermarkEntry=_BcsiIfWatermarkEntry_Object((1,3,6,1,4,1,1588,3,1,11,1,2,1))
bcsiIfWatermarkEntry.setIndexNames((0,_E,_F),(0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:bcsiIfWatermarkEntry.setStatus(_A)
class _BcsiIfWatermarkWindowType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('bcsiIfWatermarkCurrent1Hr',1),('bcsiIfWatermarkLast1Hr',2),('bcsiIfWatermarkCurrent24Hr',3),('bcsiIfWatermarkLast24Hr',4)))
_BcsiIfWatermarkWindowType_Type.__name__=_D
_BcsiIfWatermarkWindowType_Object=MibTableColumn
bcsiIfWatermarkWindowType=_BcsiIfWatermarkWindowType_Object((1,3,6,1,4,1,1588,3,1,11,1,2,1,1),_BcsiIfWatermarkWindowType_Type())
bcsiIfWatermarkWindowType.setMaxAccess(_G)
if mibBuilder.loadTexts:bcsiIfWatermarkWindowType.setStatus(_A)
class _BcsiIfWatermarkTrafficDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bcsiIfWatermarkTrafficDirIn',1),('bcsiIfWatermarkTrafficDirOut',2)))
_BcsiIfWatermarkTrafficDirection_Type.__name__=_D
_BcsiIfWatermarkTrafficDirection_Object=MibTableColumn
bcsiIfWatermarkTrafficDirection=_BcsiIfWatermarkTrafficDirection_Object((1,3,6,1,4,1,1588,3,1,11,1,2,1,2),_BcsiIfWatermarkTrafficDirection_Type())
bcsiIfWatermarkTrafficDirection.setMaxAccess(_G)
if mibBuilder.loadTexts:bcsiIfWatermarkTrafficDirection.setStatus(_A)
class _BcsiIfWatermarkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bcsiIfWatermarkTypeLow',1),('bcsiIfWatermarkTypeHigh',2)))
_BcsiIfWatermarkType_Type.__name__=_D
_BcsiIfWatermarkType_Object=MibTableColumn
bcsiIfWatermarkType=_BcsiIfWatermarkType_Object((1,3,6,1,4,1,1588,3,1,11,1,2,1,3),_BcsiIfWatermarkType_Type())
bcsiIfWatermarkType.setMaxAccess(_G)
if mibBuilder.loadTexts:bcsiIfWatermarkType.setStatus(_A)
_BcsiIfWatermarkBitRate_Type=CounterBasedGauge64
_BcsiIfWatermarkBitRate_Object=MibTableColumn
bcsiIfWatermarkBitRate=_BcsiIfWatermarkBitRate_Object((1,3,6,1,4,1,1588,3,1,11,1,2,1,4),_BcsiIfWatermarkBitRate_Type())
bcsiIfWatermarkBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiIfWatermarkBitRate.setStatus(_A)
if mibBuilder.loadTexts:bcsiIfWatermarkBitRate.setUnits('BitsPerSec')
_BcsiIfWatermarkPktRate_Type=Gauge32
_BcsiIfWatermarkPktRate_Object=MibTableColumn
bcsiIfWatermarkPktRate=_BcsiIfWatermarkPktRate_Object((1,3,6,1,4,1,1588,3,1,11,1,2,1,5),_BcsiIfWatermarkPktRate_Type())
bcsiIfWatermarkPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiIfWatermarkPktRate.setStatus(_A)
if mibBuilder.loadTexts:bcsiIfWatermarkPktRate.setUnits('PktsPerSec')
_BcsiIfWatermarkUpdateTime_Type=DateAndTime
_BcsiIfWatermarkUpdateTime_Object=MibTableColumn
bcsiIfWatermarkUpdateTime=_BcsiIfWatermarkUpdateTime_Object((1,3,6,1,4,1,1588,3,1,11,1,2,1,6),_BcsiIfWatermarkUpdateTime_Type())
bcsiIfWatermarkUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiIfWatermarkUpdateTime.setStatus(_A)
_BcsiIfWatermarkWindowStartTime_Type=DateAndTime
_BcsiIfWatermarkWindowStartTime_Object=MibTableColumn
bcsiIfWatermarkWindowStartTime=_BcsiIfWatermarkWindowStartTime_Object((1,3,6,1,4,1,1588,3,1,11,1,2,1,7),_BcsiIfWatermarkWindowStartTime_Type())
bcsiIfWatermarkWindowStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiIfWatermarkWindowStartTime.setStatus(_A)
_BcsiIfStatsConformance_ObjectIdentity=ObjectIdentity
bcsiIfStatsConformance=_BcsiIfStatsConformance_ObjectIdentity((1,3,6,1,4,1,1588,3,1,11,2))
_BcsiIfStatsCompliances_ObjectIdentity=ObjectIdentity
bcsiIfStatsCompliances=_BcsiIfStatsCompliances_ObjectIdentity((1,3,6,1,4,1,1588,3,1,11,2,1))
_BcsiIfStatsGroups_ObjectIdentity=ObjectIdentity
bcsiIfStatsGroups=_BcsiIfStatsGroups_ObjectIdentity((1,3,6,1,4,1,1588,3,1,11,2,2))
bcsiIfStatsGroup=ObjectGroup((1,3,6,1,4,1,1588,3,1,11,2,2,1))
bcsiIfStatsGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:bcsiIfStatsGroup.setStatus(_A)
bcsiIfWatermarkGroup=ObjectGroup((1,3,6,1,4,1,1588,3,1,11,2,2,2))
bcsiIfWatermarkGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:bcsiIfWatermarkGroup.setStatus(_A)
bcsiIfStatsCompliance=ModuleCompliance((1,3,6,1,4,1,1588,3,1,11,2,1,1))
bcsiIfStatsCompliance.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:bcsiIfStatsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'brocadeInterfaceStatsMIB':brocadeInterfaceStatsMIB,'bcsiIfStatsNotifications':bcsiIfStatsNotifications,'bcsiIfStatsObjects':bcsiIfStatsObjects,'bcsiIfStatsTable':bcsiIfStatsTable,'bcsiIfStatsEntry':bcsiIfStatsEntry,_K:bcsiIfStatsInBitsPerSec,_L:bcsiIfStatsOutBitsPerSec,_M:bcsiIfStatsInPktsPerSec,_N:bcsiIfStatsOutPktsPerSec,_O:bcsiIfStatsInUtilization,_P:bcsiIfStatsOutUtilization,_Q:bcsiIfStatsInJumboFrames,'bcsiIfWatermarkTable':bcsiIfWatermarkTable,'bcsiIfWatermarkEntry':bcsiIfWatermarkEntry,_H:bcsiIfWatermarkWindowType,_I:bcsiIfWatermarkTrafficDirection,_J:bcsiIfWatermarkType,_R:bcsiIfWatermarkBitRate,_S:bcsiIfWatermarkPktRate,_T:bcsiIfWatermarkUpdateTime,_U:bcsiIfWatermarkWindowStartTime,'bcsiIfStatsConformance':bcsiIfStatsConformance,'bcsiIfStatsCompliances':bcsiIfStatsCompliances,'bcsiIfStatsCompliance':bcsiIfStatsCompliance,'bcsiIfStatsGroups':bcsiIfStatsGroups,_V:bcsiIfStatsGroup,_W:bcsiIfWatermarkGroup})