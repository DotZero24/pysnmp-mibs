_C='NotificationType'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mbgSnmpRoot,=mibBuilder.importSymbols('MBG-SNMP-ROOT-MIB','mbgSnmpRoot')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_C,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_C,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_MbgNtpDisp_ObjectIdentity=ObjectIdentity
mbgNtpDisp=_MbgNtpDisp_ObjectIdentity((1,3,6,1,4,1,5597,20))
_MbgNtpDispInfo_ObjectIdentity=ObjectIdentity
mbgNtpDispInfo=_MbgNtpDispInfo_ObjectIdentity((1,3,6,1,4,1,5597,20,2))
_MbgNtpDispClockType_Type=DisplayString
_MbgNtpDispClockType_Object=MibScalar
mbgNtpDispClockType=_MbgNtpDispClockType_Object((1,3,6,1,4,1,5597,20,2,1),_MbgNtpDispClockType_Type())
mbgNtpDispClockType.setMaxAccess(_A)
if mibBuilder.loadTexts:mbgNtpDispClockType.setStatus(_B)
_MbgNtpDispClockTypeVal_Type=Integer32
_MbgNtpDispClockTypeVal_Object=MibScalar
mbgNtpDispClockTypeVal=_MbgNtpDispClockTypeVal_Object((1,3,6,1,4,1,5597,20,2,2),_MbgNtpDispClockTypeVal_Type())
mbgNtpDispClockTypeVal.setMaxAccess(_A)
if mibBuilder.loadTexts:mbgNtpDispClockTypeVal.setStatus(_B)
_MbgNtpDispMode_Type=DisplayString
_MbgNtpDispMode_Object=MibScalar
mbgNtpDispMode=_MbgNtpDispMode_Object((1,3,6,1,4,1,5597,20,2,3),_MbgNtpDispMode_Type())
mbgNtpDispMode.setMaxAccess(_A)
if mibBuilder.loadTexts:mbgNtpDispMode.setStatus(_B)
_MbgNtpDispModeVal_Type=Integer32
_MbgNtpDispModeVal_Object=MibScalar
mbgNtpDispModeVal=_MbgNtpDispModeVal_Object((1,3,6,1,4,1,5597,20,2,4),_MbgNtpDispModeVal_Type())
mbgNtpDispModeVal.setMaxAccess(_A)
if mibBuilder.loadTexts:mbgNtpDispModeVal.setStatus(_B)
_MbgNtpDispState_Type=DisplayString
_MbgNtpDispState_Object=MibScalar
mbgNtpDispState=_MbgNtpDispState_Object((1,3,6,1,4,1,5597,20,2,5),_MbgNtpDispState_Type())
mbgNtpDispState.setMaxAccess(_A)
if mibBuilder.loadTexts:mbgNtpDispState.setStatus(_B)
_MbgNtpDispTraps_ObjectIdentity=ObjectIdentity
mbgNtpDispTraps=_MbgNtpDispTraps_ObjectIdentity((1,3,6,1,4,1,5597,20,3))
mbgNtpDispTrapBoot=NotificationType((1,3,6,1,4,1,5597,20,3,0,1))
if mibBuilder.loadTexts:mbgNtpDispTrapBoot.setStatus('')
mbgNtpDispTrapSync=NotificationType((1,3,6,1,4,1,5597,20,3,0,2))
if mibBuilder.loadTexts:mbgNtpDispTrapSync.setStatus('')
mbgNtpDispTrapNotSync=NotificationType((1,3,6,1,4,1,5597,20,3,0,3))
if mibBuilder.loadTexts:mbgNtpDispTrapNotSync.setStatus('')
mbgNtpDispTrapTestNotification=NotificationType((1,3,6,1,4,1,5597,20,3,0,4))
if mibBuilder.loadTexts:mbgNtpDispTrapTestNotification.setStatus('')
mibBuilder.exportSymbols('MBG-SNMP-NTP-DISPLAY-MIB',**{'mbgNtpDisp':mbgNtpDisp,'mbgNtpDispInfo':mbgNtpDispInfo,'mbgNtpDispClockType':mbgNtpDispClockType,'mbgNtpDispClockTypeVal':mbgNtpDispClockTypeVal,'mbgNtpDispMode':mbgNtpDispMode,'mbgNtpDispModeVal':mbgNtpDispModeVal,'mbgNtpDispState':mbgNtpDispState,'mbgNtpDispTraps':mbgNtpDispTraps,'mbgNtpDispTrapBoot':mbgNtpDispTrapBoot,'mbgNtpDispTrapSync':mbgNtpDispTrapSync,'mbgNtpDispTrapNotSync':mbgNtpDispTrapNotSync,'mbgNtpDispTrapTestNotification':mbgNtpDispTrapTestNotification})