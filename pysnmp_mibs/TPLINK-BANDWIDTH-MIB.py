_N='tpRateLimitEgressRate'
_M='tpRateLimitIngressRate'
_L='tpStormControlMultiCastRate'
_K='tpStormControlBroadCastRate'
_J='tpRateLimitPort'
_I='tpStormControlPort'
_H='ifIndex'
_G='IF-MIB'
_F='OctetString'
_E='read-only'
_D='Integer32'
_C='TPLINK-BANDWIDTH-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkBandWidthMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,23))
if mibBuilder.loadTexts:tplinkBandWidthMIB.setRevisions(('2012-12-13 09:30',))
_TplinkBandWidthMIBObjects_ObjectIdentity=ObjectIdentity
tplinkBandWidthMIBObjects=_TplinkBandWidthMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,23,1))
_TpRateLimit_ObjectIdentity=ObjectIdentity
tpRateLimit=_TpRateLimit_ObjectIdentity((1,3,6,1,4,1,11863,6,23,1,1))
_TpRateLimitTable_Object=MibTable
tpRateLimitTable=_TpRateLimitTable_Object((1,3,6,1,4,1,11863,6,23,1,1,1))
if mibBuilder.loadTexts:tpRateLimitTable.setStatus(_A)
_TpRateLimitEntry_Object=MibTableRow
tpRateLimitEntry=_TpRateLimitEntry_Object((1,3,6,1,4,1,11863,6,23,1,1,1,1))
tpRateLimitEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:tpRateLimitEntry.setStatus(_A)
_TpRateLimitPort_Type=DisplayString
_TpRateLimitPort_Object=MibTableColumn
tpRateLimitPort=_TpRateLimitPort_Object((1,3,6,1,4,1,11863,6,23,1,1,1,1,1),_TpRateLimitPort_Type())
tpRateLimitPort.setMaxAccess(_E)
if mibBuilder.loadTexts:tpRateLimitPort.setStatus(_A)
class _TpRateLimitIngressRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_TpRateLimitIngressRate_Type.__name__=_D
_TpRateLimitIngressRate_Object=MibTableColumn
tpRateLimitIngressRate=_TpRateLimitIngressRate_Object((1,3,6,1,4,1,11863,6,23,1,1,1,1,2),_TpRateLimitIngressRate_Type())
tpRateLimitIngressRate.setMaxAccess(_B)
if mibBuilder.loadTexts:tpRateLimitIngressRate.setStatus(_A)
class _TpRateLimitEgressRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_TpRateLimitEgressRate_Type.__name__=_D
_TpRateLimitEgressRate_Object=MibTableColumn
tpRateLimitEgressRate=_TpRateLimitEgressRate_Object((1,3,6,1,4,1,11863,6,23,1,1,1,1,3),_TpRateLimitEgressRate_Type())
tpRateLimitEgressRate.setMaxAccess(_B)
if mibBuilder.loadTexts:tpRateLimitEgressRate.setStatus(_A)
class _TpRateLimitPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_TpRateLimitPortLag_Type.__name__=_F
_TpRateLimitPortLag_Object=MibTableColumn
tpRateLimitPortLag=_TpRateLimitPortLag_Object((1,3,6,1,4,1,11863,6,23,1,1,1,1,4),_TpRateLimitPortLag_Type())
tpRateLimitPortLag.setMaxAccess(_E)
if mibBuilder.loadTexts:tpRateLimitPortLag.setStatus(_A)
_TpStormControl_ObjectIdentity=ObjectIdentity
tpStormControl=_TpStormControl_ObjectIdentity((1,3,6,1,4,1,11863,6,23,1,2))
_TpStormControlTable_Object=MibTable
tpStormControlTable=_TpStormControlTable_Object((1,3,6,1,4,1,11863,6,23,1,2,1))
if mibBuilder.loadTexts:tpStormControlTable.setStatus(_A)
_TpStormControlEntry_Object=MibTableRow
tpStormControlEntry=_TpStormControlEntry_Object((1,3,6,1,4,1,11863,6,23,1,2,1,1))
tpStormControlEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:tpStormControlEntry.setStatus(_A)
_TpStormControlPort_Type=DisplayString
_TpStormControlPort_Object=MibTableColumn
tpStormControlPort=_TpStormControlPort_Object((1,3,6,1,4,1,11863,6,23,1,2,1,1,1),_TpStormControlPort_Type())
tpStormControlPort.setMaxAccess(_E)
if mibBuilder.loadTexts:tpStormControlPort.setStatus(_A)
class _TpStormControlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('kbps',0),('ratio',1),('pps',2)))
_TpStormControlMode_Type.__name__=_D
_TpStormControlMode_Object=MibTableColumn
tpStormControlMode=_TpStormControlMode_Object((1,3,6,1,4,1,11863,6,23,1,2,1,1,2),_TpStormControlMode_Type())
tpStormControlMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tpStormControlMode.setStatus(_A)
_TpStormControlBroadCastRate_Type=Integer32
_TpStormControlBroadCastRate_Object=MibTableColumn
tpStormControlBroadCastRate=_TpStormControlBroadCastRate_Object((1,3,6,1,4,1,11863,6,23,1,2,1,1,3),_TpStormControlBroadCastRate_Type())
tpStormControlBroadCastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:tpStormControlBroadCastRate.setStatus(_A)
class _TpStormControlMultiCastRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1488000))
_TpStormControlMultiCastRate_Type.__name__=_D
_TpStormControlMultiCastRate_Object=MibTableColumn
tpStormControlMultiCastRate=_TpStormControlMultiCastRate_Object((1,3,6,1,4,1,11863,6,23,1,2,1,1,4),_TpStormControlMultiCastRate_Type())
tpStormControlMultiCastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:tpStormControlMultiCastRate.setStatus(_A)
class _TpStormControlULRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1488000))
_TpStormControlULRate_Type.__name__=_D
_TpStormControlULRate_Object=MibTableColumn
tpStormControlULRate=_TpStormControlULRate_Object((1,3,6,1,4,1,11863,6,23,1,2,1,1,5),_TpStormControlULRate_Type())
tpStormControlULRate.setMaxAccess(_B)
if mibBuilder.loadTexts:tpStormControlULRate.setStatus(_A)
class _TpStormControlAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('drop',0),('shutdown',1)))
_TpStormControlAction_Type.__name__=_D
_TpStormControlAction_Object=MibTableColumn
tpStormControlAction=_TpStormControlAction_Object((1,3,6,1,4,1,11863,6,23,1,2,1,1,6),_TpStormControlAction_Type())
tpStormControlAction.setMaxAccess(_B)
if mibBuilder.loadTexts:tpStormControlAction.setStatus(_A)
_TpStormControlRecoverTime_Type=Integer32
_TpStormControlRecoverTime_Object=MibTableColumn
tpStormControlRecoverTime=_TpStormControlRecoverTime_Object((1,3,6,1,4,1,11863,6,23,1,2,1,1,7),_TpStormControlRecoverTime_Type())
tpStormControlRecoverTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tpStormControlRecoverTime.setStatus(_A)
class _TpStormControlPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_TpStormControlPortLag_Type.__name__=_F
_TpStormControlPortLag_Object=MibTableColumn
tpStormControlPortLag=_TpStormControlPortLag_Object((1,3,6,1,4,1,11863,6,23,1,2,1,1,8),_TpStormControlPortLag_Type())
tpStormControlPortLag.setMaxAccess(_E)
if mibBuilder.loadTexts:tpStormControlPortLag.setStatus(_A)
_TpStormControlRecover_ObjectIdentity=ObjectIdentity
tpStormControlRecover=_TpStormControlRecover_ObjectIdentity((1,3,6,1,4,1,11863,6,23,1,3))
_TpStormControlRecoverPort_Type=OctetString
_TpStormControlRecoverPort_Object=MibScalar
tpStormControlRecoverPort=_TpStormControlRecoverPort_Object((1,3,6,1,4,1,11863,6,23,1,3,1),_TpStormControlRecoverPort_Type())
tpStormControlRecoverPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tpStormControlRecoverPort.setStatus(_A)
_TplinkBandWidthNotifications_ObjectIdentity=ObjectIdentity
tplinkBandWidthNotifications=_TplinkBandWidthNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,23,2))
tpBroadcastRateExceed=NotificationType((1,3,6,1,4,1,11863,6,23,2,1))
tpBroadcastRateExceed.setObjects(*((_C,_I),(_C,_K)))
if mibBuilder.loadTexts:tpBroadcastRateExceed.setStatus(_A)
tpMulticastRateExceed=NotificationType((1,3,6,1,4,1,11863,6,23,2,2))
tpMulticastRateExceed.setObjects(*((_C,_I),(_C,_L)))
if mibBuilder.loadTexts:tpMulticastRateExceed.setStatus(_A)
tpIngressRateExceed=NotificationType((1,3,6,1,4,1,11863,6,23,2,3))
tpIngressRateExceed.setObjects(*((_C,_J),(_C,_M)))
if mibBuilder.loadTexts:tpIngressRateExceed.setStatus(_A)
tpEgressRateExceed=NotificationType((1,3,6,1,4,1,11863,6,23,2,4))
tpEgressRateExceed.setObjects(*((_C,_J),(_C,_N)))
if mibBuilder.loadTexts:tpEgressRateExceed.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'tplinkBandWidthMIB':tplinkBandWidthMIB,'tplinkBandWidthMIBObjects':tplinkBandWidthMIBObjects,'tpRateLimit':tpRateLimit,'tpRateLimitTable':tpRateLimitTable,'tpRateLimitEntry':tpRateLimitEntry,_J:tpRateLimitPort,_M:tpRateLimitIngressRate,_N:tpRateLimitEgressRate,'tpRateLimitPortLag':tpRateLimitPortLag,'tpStormControl':tpStormControl,'tpStormControlTable':tpStormControlTable,'tpStormControlEntry':tpStormControlEntry,_I:tpStormControlPort,'tpStormControlMode':tpStormControlMode,_K:tpStormControlBroadCastRate,_L:tpStormControlMultiCastRate,'tpStormControlULRate':tpStormControlULRate,'tpStormControlAction':tpStormControlAction,'tpStormControlRecoverTime':tpStormControlRecoverTime,'tpStormControlPortLag':tpStormControlPortLag,'tpStormControlRecover':tpStormControlRecover,'tpStormControlRecoverPort':tpStormControlRecoverPort,'tplinkBandWidthNotifications':tplinkBandWidthNotifications,'tpBroadcastRateExceed':tpBroadcastRateExceed,'tpMulticastRateExceed':tpMulticastRateExceed,'tpIngressRateExceed':tpIngressRateExceed,'tpEgressRateExceed':tpEgressRateExceed})