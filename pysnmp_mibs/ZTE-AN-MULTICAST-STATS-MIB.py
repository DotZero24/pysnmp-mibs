_I='zxAnMCastGrpTrafficGrpIpAddr'
_H='zxAnMCastGrpTrafficGrpIpType'
_G='zxAnMCastGrpTrafficVid'
_F='not-accessible'
_E='Integer32'
_D='ZTE-AN-MULTICAST-STATS-MIB'
_C='read-only'
_B='kbps'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
zxAn,=mibBuilder.importSymbols('ZTE-AN-TC-MIB','zxAn')
zxAnMulticastStatsMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,45))
if mibBuilder.loadTexts:zxAnMulticastStatsMib.setRevisions(('2012-09-14 14:30',))
_ZxAnMulticastStatsObjects_ObjectIdentity=ObjectIdentity
zxAnMulticastStatsObjects=_ZxAnMulticastStatsObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,45,2))
_ZxAnMulticastGroupStats_ObjectIdentity=ObjectIdentity
zxAnMulticastGroupStats=_ZxAnMulticastGroupStats_ObjectIdentity((1,3,6,1,4,1,3902,1015,45,2,2))
_ZxAnMcastGrpTrafficTable_Object=MibTable
zxAnMcastGrpTrafficTable=_ZxAnMcastGrpTrafficTable_Object((1,3,6,1,4,1,3902,1015,45,2,2,2))
if mibBuilder.loadTexts:zxAnMcastGrpTrafficTable.setStatus(_A)
_ZxAnMcastGrpTrafficEntry_Object=MibTableRow
zxAnMcastGrpTrafficEntry=_ZxAnMcastGrpTrafficEntry_Object((1,3,6,1,4,1,3902,1015,45,2,2,2,1))
zxAnMcastGrpTrafficEntry.setIndexNames((0,_D,_G),(0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:zxAnMcastGrpTrafficEntry.setStatus(_A)
class _ZxAnMCastGrpTrafficVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnMCastGrpTrafficVid_Type.__name__=_E
_ZxAnMCastGrpTrafficVid_Object=MibTableColumn
zxAnMCastGrpTrafficVid=_ZxAnMCastGrpTrafficVid_Object((1,3,6,1,4,1,3902,1015,45,2,2,2,1,1),_ZxAnMCastGrpTrafficVid_Type())
zxAnMCastGrpTrafficVid.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnMCastGrpTrafficVid.setStatus(_A)
_ZxAnMCastGrpTrafficGrpIpType_Type=InetAddressType
_ZxAnMCastGrpTrafficGrpIpType_Object=MibTableColumn
zxAnMCastGrpTrafficGrpIpType=_ZxAnMCastGrpTrafficGrpIpType_Object((1,3,6,1,4,1,3902,1015,45,2,2,2,1,2),_ZxAnMCastGrpTrafficGrpIpType_Type())
zxAnMCastGrpTrafficGrpIpType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnMCastGrpTrafficGrpIpType.setStatus(_A)
_ZxAnMCastGrpTrafficGrpIpAddr_Type=InetAddress
_ZxAnMCastGrpTrafficGrpIpAddr_Object=MibTableColumn
zxAnMCastGrpTrafficGrpIpAddr=_ZxAnMCastGrpTrafficGrpIpAddr_Object((1,3,6,1,4,1,3902,1015,45,2,2,2,1,3),_ZxAnMCastGrpTrafficGrpIpAddr_Type())
zxAnMCastGrpTrafficGrpIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnMCastGrpTrafficGrpIpAddr.setStatus(_A)
class _ZxAnMCastGrpTrafficUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pps',1),(_B,2)))
_ZxAnMCastGrpTrafficUnit_Type.__name__=_E
_ZxAnMCastGrpTrafficUnit_Object=MibTableColumn
zxAnMCastGrpTrafficUnit=_ZxAnMCastGrpTrafficUnit_Object((1,3,6,1,4,1,3902,1015,45,2,2,2,1,4),_ZxAnMCastGrpTrafficUnit_Type())
zxAnMCastGrpTrafficUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMCastGrpTrafficUnit.setStatus(_A)
_ZxAnMCastGrpTrafficPeakRate_Type=Integer32
_ZxAnMCastGrpTrafficPeakRate_Object=MibTableColumn
zxAnMCastGrpTrafficPeakRate=_ZxAnMCastGrpTrafficPeakRate_Object((1,3,6,1,4,1,3902,1015,45,2,2,2,1,5),_ZxAnMCastGrpTrafficPeakRate_Type())
zxAnMCastGrpTrafficPeakRate.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMCastGrpTrafficPeakRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnMCastGrpTrafficPeakRate.setUnits(_B)
_ZxAnMCastGrpTrafficAvgRate_Type=Integer32
_ZxAnMCastGrpTrafficAvgRate_Object=MibTableColumn
zxAnMCastGrpTrafficAvgRate=_ZxAnMCastGrpTrafficAvgRate_Object((1,3,6,1,4,1,3902,1015,45,2,2,2,1,6),_ZxAnMCastGrpTrafficAvgRate_Type())
zxAnMCastGrpTrafficAvgRate.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMCastGrpTrafficAvgRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnMCastGrpTrafficAvgRate.setUnits(_B)
_ZxAnMCastGrpTrafficCurrRate_Type=Integer32
_ZxAnMCastGrpTrafficCurrRate_Object=MibTableColumn
zxAnMCastGrpTrafficCurrRate=_ZxAnMCastGrpTrafficCurrRate_Object((1,3,6,1,4,1,3902,1015,45,2,2,2,1,7),_ZxAnMCastGrpTrafficCurrRate_Type())
zxAnMCastGrpTrafficCurrRate.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMCastGrpTrafficCurrRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnMCastGrpTrafficCurrRate.setUnits(_B)
_ZxAnMCastGrpTrafficMinRate_Type=Integer32
_ZxAnMCastGrpTrafficMinRate_Object=MibTableColumn
zxAnMCastGrpTrafficMinRate=_ZxAnMCastGrpTrafficMinRate_Object((1,3,6,1,4,1,3902,1015,45,2,2,2,1,8),_ZxAnMCastGrpTrafficMinRate_Type())
zxAnMCastGrpTrafficMinRate.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMCastGrpTrafficMinRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnMCastGrpTrafficMinRate.setUnits(_B)
_ZxAnMCastGrpTrafficRowStatus_Type=RowStatus
_ZxAnMCastGrpTrafficRowStatus_Object=MibTableColumn
zxAnMCastGrpTrafficRowStatus=_ZxAnMCastGrpTrafficRowStatus_Object((1,3,6,1,4,1,3902,1015,45,2,2,2,1,50),_ZxAnMCastGrpTrafficRowStatus_Type())
zxAnMCastGrpTrafficRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zxAnMCastGrpTrafficRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zxAnMulticastStatsMib':zxAnMulticastStatsMib,'zxAnMulticastStatsObjects':zxAnMulticastStatsObjects,'zxAnMulticastGroupStats':zxAnMulticastGroupStats,'zxAnMcastGrpTrafficTable':zxAnMcastGrpTrafficTable,'zxAnMcastGrpTrafficEntry':zxAnMcastGrpTrafficEntry,_G:zxAnMCastGrpTrafficVid,_H:zxAnMCastGrpTrafficGrpIpType,_I:zxAnMCastGrpTrafficGrpIpAddr,'zxAnMCastGrpTrafficUnit':zxAnMCastGrpTrafficUnit,'zxAnMCastGrpTrafficPeakRate':zxAnMCastGrpTrafficPeakRate,'zxAnMCastGrpTrafficAvgRate':zxAnMCastGrpTrafficAvgRate,'zxAnMCastGrpTrafficCurrRate':zxAnMCastGrpTrafficCurrRate,'zxAnMCastGrpTrafficMinRate':zxAnMCastGrpTrafficMinRate,'zxAnMCastGrpTrafficRowStatus':zxAnMCastGrpTrafficRowStatus})