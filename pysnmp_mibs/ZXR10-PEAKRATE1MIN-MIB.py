_H='read-write'
_G='portIfOutIndex'
_F='ZXR10-PEAKRATE1MIN-MIB'
_E='DisplayString'
_D='Integer32'
_C='ppm'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_Zxr10_ObjectIdentity=ObjectIdentity
zxr10=_Zxr10_ObjectIdentity((1,3,6,1,4,1,3902,3))
_Zxr10switch_ObjectIdentity=ObjectIdentity
zxr10switch=_Zxr10switch_ObjectIdentity((1,3,6,1,4,1,3902,3,102))
_Zxr10Peakrate1Min_ObjectIdentity=ObjectIdentity
zxr10Peakrate1Min=_Zxr10Peakrate1Min_ObjectIdentity((1,3,6,1,4,1,3902,3,102,31))
_PortPeakrateTable_Object=MibTable
portPeakrateTable=_PortPeakrateTable_Object((1,3,6,1,4,1,3902,3,102,31,1))
if mibBuilder.loadTexts:portPeakrateTable.setStatus(_A)
_PortPeakrateEntry_Object=MibTableRow
portPeakrateEntry=_PortPeakrateEntry_Object((1,3,6,1,4,1,3902,3,102,31,1,1))
portPeakrateEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:portPeakrateEntry.setStatus(_A)
class _PortIfOutIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortIfOutIndex_Type.__name__=_D
_PortIfOutIndex_Object=MibTableColumn
portIfOutIndex=_PortIfOutIndex_Object((1,3,6,1,4,1,3902,3,102,31,1,1,1),_PortIfOutIndex_Type())
portIfOutIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:portIfOutIndex.setStatus(_A)
class _PortPeakrateEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_PortPeakrateEnable_Type.__name__=_D
_PortPeakrateEnable_Object=MibTableColumn
portPeakrateEnable=_PortPeakrateEnable_Object((1,3,6,1,4,1,3902,3,102,31,1,1,2),_PortPeakrateEnable_Type())
portPeakrateEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:portPeakrateEnable.setStatus(_A)
_PortInUnicastPktsPeak_Type=Counter64
_PortInUnicastPktsPeak_Object=MibTableColumn
portInUnicastPktsPeak=_PortInUnicastPktsPeak_Object((1,3,6,1,4,1,3902,3,102,31,1,1,3),_PortInUnicastPktsPeak_Type())
portInUnicastPktsPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:portInUnicastPktsPeak.setStatus(_A)
if mibBuilder.loadTexts:portInUnicastPktsPeak.setUnits(_C)
_PortInUnicastTime_Type=OctetString
_PortInUnicastTime_Object=MibTableColumn
portInUnicastTime=_PortInUnicastTime_Object((1,3,6,1,4,1,3902,3,102,31,1,1,4),_PortInUnicastTime_Type())
portInUnicastTime.setMaxAccess(_B)
if mibBuilder.loadTexts:portInUnicastTime.setStatus(_A)
_PortInMulticastPktsPeak_Type=Counter64
_PortInMulticastPktsPeak_Object=MibTableColumn
portInMulticastPktsPeak=_PortInMulticastPktsPeak_Object((1,3,6,1,4,1,3902,3,102,31,1,1,5),_PortInMulticastPktsPeak_Type())
portInMulticastPktsPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:portInMulticastPktsPeak.setStatus(_A)
if mibBuilder.loadTexts:portInMulticastPktsPeak.setUnits(_C)
_PortInMulticastTime_Type=OctetString
_PortInMulticastTime_Object=MibTableColumn
portInMulticastTime=_PortInMulticastTime_Object((1,3,6,1,4,1,3902,3,102,31,1,1,6),_PortInMulticastTime_Type())
portInMulticastTime.setMaxAccess(_B)
if mibBuilder.loadTexts:portInMulticastTime.setStatus(_A)
_PortInBroadcastPktsPeak_Type=Counter64
_PortInBroadcastPktsPeak_Object=MibTableColumn
portInBroadcastPktsPeak=_PortInBroadcastPktsPeak_Object((1,3,6,1,4,1,3902,3,102,31,1,1,7),_PortInBroadcastPktsPeak_Type())
portInBroadcastPktsPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:portInBroadcastPktsPeak.setStatus(_A)
if mibBuilder.loadTexts:portInBroadcastPktsPeak.setUnits(_C)
_PortInBroadcastTime_Type=OctetString
_PortInBroadcastTime_Object=MibTableColumn
portInBroadcastTime=_PortInBroadcastTime_Object((1,3,6,1,4,1,3902,3,102,31,1,1,8),_PortInBroadcastTime_Type())
portInBroadcastTime.setMaxAccess(_B)
if mibBuilder.loadTexts:portInBroadcastTime.setStatus(_A)
_PortInTotalErrPktsPeak_Type=Counter64
_PortInTotalErrPktsPeak_Object=MibTableColumn
portInTotalErrPktsPeak=_PortInTotalErrPktsPeak_Object((1,3,6,1,4,1,3902,3,102,31,1,1,9),_PortInTotalErrPktsPeak_Type())
portInTotalErrPktsPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:portInTotalErrPktsPeak.setStatus(_A)
if mibBuilder.loadTexts:portInTotalErrPktsPeak.setUnits(_C)
_PortInTotalErrTime_Type=OctetString
_PortInTotalErrTime_Object=MibTableColumn
portInTotalErrTime=_PortInTotalErrTime_Object((1,3,6,1,4,1,3902,3,102,31,1,1,10),_PortInTotalErrTime_Type())
portInTotalErrTime.setMaxAccess(_B)
if mibBuilder.loadTexts:portInTotalErrTime.setStatus(_A)
_PortOutUnicastPktsPeak_Type=Counter64
_PortOutUnicastPktsPeak_Object=MibTableColumn
portOutUnicastPktsPeak=_PortOutUnicastPktsPeak_Object((1,3,6,1,4,1,3902,3,102,31,1,1,11),_PortOutUnicastPktsPeak_Type())
portOutUnicastPktsPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:portOutUnicastPktsPeak.setStatus(_A)
if mibBuilder.loadTexts:portOutUnicastPktsPeak.setUnits(_C)
_PortOutUnicastTime_Type=OctetString
_PortOutUnicastTime_Object=MibTableColumn
portOutUnicastTime=_PortOutUnicastTime_Object((1,3,6,1,4,1,3902,3,102,31,1,1,12),_PortOutUnicastTime_Type())
portOutUnicastTime.setMaxAccess(_B)
if mibBuilder.loadTexts:portOutUnicastTime.setStatus(_A)
_PortOutMulticastPktsPeak_Type=Counter64
_PortOutMulticastPktsPeak_Object=MibTableColumn
portOutMulticastPktsPeak=_PortOutMulticastPktsPeak_Object((1,3,6,1,4,1,3902,3,102,31,1,1,13),_PortOutMulticastPktsPeak_Type())
portOutMulticastPktsPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:portOutMulticastPktsPeak.setStatus(_A)
if mibBuilder.loadTexts:portOutMulticastPktsPeak.setUnits(_C)
_PortOutMulticastTime_Type=OctetString
_PortOutMulticastTime_Object=MibTableColumn
portOutMulticastTime=_PortOutMulticastTime_Object((1,3,6,1,4,1,3902,3,102,31,1,1,14),_PortOutMulticastTime_Type())
portOutMulticastTime.setMaxAccess(_B)
if mibBuilder.loadTexts:portOutMulticastTime.setStatus(_A)
_PortOutBroadcastPktsPeak_Type=Counter64
_PortOutBroadcastPktsPeak_Object=MibTableColumn
portOutBroadcastPktsPeak=_PortOutBroadcastPktsPeak_Object((1,3,6,1,4,1,3902,3,102,31,1,1,15),_PortOutBroadcastPktsPeak_Type())
portOutBroadcastPktsPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:portOutBroadcastPktsPeak.setStatus(_A)
if mibBuilder.loadTexts:portOutBroadcastPktsPeak.setUnits(_C)
_PortOutBroadcastTime_Type=OctetString
_PortOutBroadcastTime_Object=MibTableColumn
portOutBroadcastTime=_PortOutBroadcastTime_Object((1,3,6,1,4,1,3902,3,102,31,1,1,16),_PortOutBroadcastTime_Type())
portOutBroadcastTime.setMaxAccess(_B)
if mibBuilder.loadTexts:portOutBroadcastTime.setStatus(_A)
_PortOutTotalErrPktsPeak_Type=Counter64
_PortOutTotalErrPktsPeak_Object=MibTableColumn
portOutTotalErrPktsPeak=_PortOutTotalErrPktsPeak_Object((1,3,6,1,4,1,3902,3,102,31,1,1,17),_PortOutTotalErrPktsPeak_Type())
portOutTotalErrPktsPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:portOutTotalErrPktsPeak.setStatus(_A)
if mibBuilder.loadTexts:portOutTotalErrPktsPeak.setUnits(_C)
_PortOutTotalErrTime_Type=OctetString
_PortOutTotalErrTime_Object=MibTableColumn
portOutTotalErrTime=_PortOutTotalErrTime_Object((1,3,6,1,4,1,3902,3,102,31,1,1,18),_PortOutTotalErrTime_Type())
portOutTotalErrTime.setMaxAccess(_B)
if mibBuilder.loadTexts:portOutTotalErrTime.setStatus(_A)
class _PortClearPeakPkts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('clear',0))
_PortClearPeakPkts_Type.__name__=_D
_PortClearPeakPkts_Object=MibTableColumn
portClearPeakPkts=_PortClearPeakPkts_Object((1,3,6,1,4,1,3902,3,102,31,1,1,19),_PortClearPeakPkts_Type())
portClearPeakPkts.setMaxAccess(_H)
if mibBuilder.loadTexts:portClearPeakPkts.setStatus(_A)
mibBuilder.exportSymbols(_F,**{_E:DisplayString,'zte':zte,'zxr10':zxr10,'zxr10switch':zxr10switch,'zxr10Peakrate1Min':zxr10Peakrate1Min,'portPeakrateTable':portPeakrateTable,'portPeakrateEntry':portPeakrateEntry,_G:portIfOutIndex,'portPeakrateEnable':portPeakrateEnable,'portInUnicastPktsPeak':portInUnicastPktsPeak,'portInUnicastTime':portInUnicastTime,'portInMulticastPktsPeak':portInMulticastPktsPeak,'portInMulticastTime':portInMulticastTime,'portInBroadcastPktsPeak':portInBroadcastPktsPeak,'portInBroadcastTime':portInBroadcastTime,'portInTotalErrPktsPeak':portInTotalErrPktsPeak,'portInTotalErrTime':portInTotalErrTime,'portOutUnicastPktsPeak':portOutUnicastPktsPeak,'portOutUnicastTime':portOutUnicastTime,'portOutMulticastPktsPeak':portOutMulticastPktsPeak,'portOutMulticastTime':portOutMulticastTime,'portOutBroadcastPktsPeak':portOutBroadcastPktsPeak,'portOutBroadcastTime':portOutBroadcastTime,'portOutTotalErrPktsPeak':portOutTotalErrPktsPeak,'portOutTotalErrTime':portOutTotalErrTime,'portClearPeakPkts':portClearPeakPkts})