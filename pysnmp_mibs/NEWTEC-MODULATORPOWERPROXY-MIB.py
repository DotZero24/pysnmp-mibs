_J='ntcModPwrProxyConfGrpV1Standard'
_I='ntcModPowerProxyPowerReqCounter'
_H='ntcModPowerProxyCurModPower'
_G='ntcModPowerProxyRmtUpcState'
_F='ntcModPowerProxyEnable'
_E='NtcEnable'
_D='read-only'
_C='Integer32'
_B='NEWTEC-MODULATORPOWERPROXY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcEnable,=mibBuilder.importSymbols('NEWTEC-TC-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntcModulatorPowerProxy=ModuleIdentity((1,3,6,1,4,1,5835,5,2,3400))
if mibBuilder.loadTexts:ntcModulatorPowerProxy.setRevisions(('2013-05-22 06:00',))
_NtcModulatorPowerProxyObjects_ObjectIdentity=ObjectIdentity
ntcModulatorPowerProxyObjects=_NtcModulatorPowerProxyObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3400,1))
if mibBuilder.loadTexts:ntcModulatorPowerProxyObjects.setStatus(_A)
class _NtcModPowerProxyEnable_Type(NtcEnable):defaultValue=0
_NtcModPowerProxyEnable_Type.__name__=_E
_NtcModPowerProxyEnable_Object=MibScalar
ntcModPowerProxyEnable=_NtcModPowerProxyEnable_Object((1,3,6,1,4,1,5835,5,2,3400,1,1),_NtcModPowerProxyEnable_Type())
ntcModPowerProxyEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:ntcModPowerProxyEnable.setStatus(_A)
_NtcModPowerProxyMonitoring_ObjectIdentity=ObjectIdentity
ntcModPowerProxyMonitoring=_NtcModPowerProxyMonitoring_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3400,1,2))
if mibBuilder.loadTexts:ntcModPowerProxyMonitoring.setStatus(_A)
class _NtcModPowerProxyRmtUpcState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_NtcModPowerProxyRmtUpcState_Type.__name__=_C
_NtcModPowerProxyRmtUpcState_Object=MibScalar
ntcModPowerProxyRmtUpcState=_NtcModPowerProxyRmtUpcState_Object((1,3,6,1,4,1,5835,5,2,3400,1,2,1),_NtcModPowerProxyRmtUpcState_Type())
ntcModPowerProxyRmtUpcState.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcModPowerProxyRmtUpcState.setStatus(_A)
class _NtcModPowerProxyCurModPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-350,100))
_NtcModPowerProxyCurModPower_Type.__name__=_C
_NtcModPowerProxyCurModPower_Object=MibScalar
ntcModPowerProxyCurModPower=_NtcModPowerProxyCurModPower_Object((1,3,6,1,4,1,5835,5,2,3400,1,2,2),_NtcModPowerProxyCurModPower_Type())
ntcModPowerProxyCurModPower.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcModPowerProxyCurModPower.setStatus(_A)
if mibBuilder.loadTexts:ntcModPowerProxyCurModPower.setUnits('dBm')
_NtcModPowerProxyPowerReqCounter_Type=Counter64
_NtcModPowerProxyPowerReqCounter_Object=MibScalar
ntcModPowerProxyPowerReqCounter=_NtcModPowerProxyPowerReqCounter_Object((1,3,6,1,4,1,5835,5,2,3400,1,2,3),_NtcModPowerProxyPowerReqCounter_Type())
ntcModPowerProxyPowerReqCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcModPowerProxyPowerReqCounter.setStatus(_A)
_NtcModPwrProxyConformance_ObjectIdentity=ObjectIdentity
ntcModPwrProxyConformance=_NtcModPwrProxyConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3400,2))
if mibBuilder.loadTexts:ntcModPwrProxyConformance.setStatus(_A)
_NtcModPwrProxyConfCompliance_ObjectIdentity=ObjectIdentity
ntcModPwrProxyConfCompliance=_NtcModPwrProxyConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3400,2,1))
if mibBuilder.loadTexts:ntcModPwrProxyConfCompliance.setStatus(_A)
_NtcModPwrProxyConfGroup_ObjectIdentity=ObjectIdentity
ntcModPwrProxyConfGroup=_NtcModPwrProxyConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3400,2,2))
if mibBuilder.loadTexts:ntcModPwrProxyConfGroup.setStatus(_A)
ntcModPwrProxyConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,3400,2,2,1))
ntcModPwrProxyConfGrpV1Standard.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:ntcModPwrProxyConfGrpV1Standard.setStatus(_A)
ntcModPwrProxyConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,3400,2,1,1))
ntcModPwrProxyConfCompV1Standard.setObjects((_B,_J))
if mibBuilder.loadTexts:ntcModPwrProxyConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcModulatorPowerProxy':ntcModulatorPowerProxy,'ntcModulatorPowerProxyObjects':ntcModulatorPowerProxyObjects,_F:ntcModPowerProxyEnable,'ntcModPowerProxyMonitoring':ntcModPowerProxyMonitoring,_G:ntcModPowerProxyRmtUpcState,_H:ntcModPowerProxyCurModPower,_I:ntcModPowerProxyPowerReqCounter,'ntcModPwrProxyConformance':ntcModPwrProxyConformance,'ntcModPwrProxyConfCompliance':ntcModPwrProxyConfCompliance,'ntcModPwrProxyConfCompV1Standard':ntcModPwrProxyConfCompV1Standard,'ntcModPwrProxyConfGroup':ntcModPwrProxyConfGroup,_J:ntcModPwrProxyConfGrpV1Standard})