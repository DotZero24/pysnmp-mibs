_I='NotificationType'
_H='omeAlertSeverity'
_G='omeRawAlertInfo'
_F='omeAlertDataSources'
_E='mandatory'
_D='read-only'
_C='omeAlertDevice'
_B='omeAlertMessage'
_A='MIB-Dell-OME'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_I,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_I,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class DellString(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
class DellString1(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Dell_ObjectIdentity=ObjectIdentity
dell=_Dell_ObjectIdentity((1,3,6,1,4,1,674))
_EnterpriseSW_ObjectIdentity=ObjectIdentity
enterpriseSW=_EnterpriseSW_ObjectIdentity((1,3,6,1,4,1,674,11000))
_SysMgmtBranch_ObjectIdentity=ObjectIdentity
sysMgmtBranch=_SysMgmtBranch_ObjectIdentity((1,3,6,1,4,1,674,11000,1000))
_OmEssentialsMIB_ObjectIdentity=ObjectIdentity
omEssentialsMIB=_OmEssentialsMIB_ObjectIdentity((1,3,6,1,4,1,674,11000,1000,100))
_OmEssentialsTrap_ObjectIdentity=ObjectIdentity
omEssentialsTrap=_OmEssentialsTrap_ObjectIdentity((1,3,6,1,4,1,674,11000,1000,100,1))
_OmeAlertMessage_Type=DellString
_OmeAlertMessage_Object=MibScalar
omeAlertMessage=_OmeAlertMessage_Object((1,3,6,1,4,1,674,11000,1000,100,1,1),_OmeAlertMessage_Type())
omeAlertMessage.setMaxAccess(_D)
if mibBuilder.loadTexts:omeAlertMessage.setStatus(_E)
_OmeAlertDevice_Type=DellString
_OmeAlertDevice_Object=MibScalar
omeAlertDevice=_OmeAlertDevice_Object((1,3,6,1,4,1,674,11000,1000,100,1,2),_OmeAlertDevice_Type())
omeAlertDevice.setMaxAccess(_D)
if mibBuilder.loadTexts:omeAlertDevice.setStatus(_E)
_OmeAlertSeverity_Type=DellString1
_OmeAlertSeverity_Object=MibScalar
omeAlertSeverity=_OmeAlertSeverity_Object((1,3,6,1,4,1,674,11000,1000,100,1,3),_OmeAlertSeverity_Type())
omeAlertSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:omeAlertSeverity.setStatus(_E)
_OmeAlertDataSources_Type=DellString
_OmeAlertDataSources_Object=MibScalar
omeAlertDataSources=_OmeAlertDataSources_Object((1,3,6,1,4,1,674,11000,1000,100,1,4),_OmeAlertDataSources_Type())
omeAlertDataSources.setMaxAccess(_D)
if mibBuilder.loadTexts:omeAlertDataSources.setStatus(_E)
_OmeRawAlertInfo_Type=DellString
_OmeRawAlertInfo_Object=MibScalar
omeRawAlertInfo=_OmeRawAlertInfo_Object((1,3,6,1,4,1,674,11000,1000,100,1,5),_OmeRawAlertInfo_Type())
omeRawAlertInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:omeRawAlertInfo.setStatus(_E)
omeTestAlert=NotificationType((1,3,6,1,4,1,674,11000,1000,100,1,0,1))
omeTestAlert.setObjects(*((_A,_B),(_A,_C),(_A,_H)))
if mibBuilder.loadTexts:omeTestAlert.setStatus('')
omeAlertSystemUp=NotificationType((1,3,6,1,4,1,674,11000,1000,100,1,0,1000))
omeAlertSystemUp.setObjects(*((_A,_B),(_A,_C)))
if mibBuilder.loadTexts:omeAlertSystemUp.setStatus('')
omeAlertSystemDown=NotificationType((1,3,6,1,4,1,674,11000,1000,100,1,0,1001))
omeAlertSystemDown.setObjects(*((_A,_B),(_A,_C)))
if mibBuilder.loadTexts:omeAlertSystemDown.setStatus('')
omeAlertForwardedAlert=NotificationType((1,3,6,1,4,1,674,11000,1000,100,1,0,2000))
omeAlertForwardedAlert.setObjects(*((_A,_B),(_A,_C),(_A,_H)))
if mibBuilder.loadTexts:omeAlertForwardedAlert.setStatus('')
omeAlertUnknownStatus=NotificationType((1,3,6,1,4,1,674,11000,1000,100,1,0,3001))
omeAlertUnknownStatus.setObjects(*((_A,_B),(_A,_C),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:omeAlertUnknownStatus.setStatus('')
omeAlertNormalStatus=NotificationType((1,3,6,1,4,1,674,11000,1000,100,1,0,3002))
omeAlertNormalStatus.setObjects(*((_A,_B),(_A,_C),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:omeAlertNormalStatus.setStatus('')
omeAlertWarningStatus=NotificationType((1,3,6,1,4,1,674,11000,1000,100,1,0,3003))
omeAlertWarningStatus.setObjects(*((_A,_B),(_A,_C),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:omeAlertWarningStatus.setStatus('')
omeAlertCriticalStatus=NotificationType((1,3,6,1,4,1,674,11000,1000,100,1,0,3004))
omeAlertCriticalStatus.setObjects(*((_A,_B),(_A,_C),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:omeAlertCriticalStatus.setStatus('')
mibBuilder.exportSymbols(_A,**{'DellString':DellString,'DellString1':DellString1,'dell':dell,'enterpriseSW':enterpriseSW,'sysMgmtBranch':sysMgmtBranch,'omEssentialsMIB':omEssentialsMIB,'omEssentialsTrap':omEssentialsTrap,'omeTestAlert':omeTestAlert,'omeAlertSystemUp':omeAlertSystemUp,'omeAlertSystemDown':omeAlertSystemDown,'omeAlertForwardedAlert':omeAlertForwardedAlert,'omeAlertUnknownStatus':omeAlertUnknownStatus,'omeAlertNormalStatus':omeAlertNormalStatus,'omeAlertWarningStatus':omeAlertWarningStatus,'omeAlertCriticalStatus':omeAlertCriticalStatus,_B:omeAlertMessage,_C:omeAlertDevice,_H:omeAlertSeverity,_F:omeAlertDataSources,_G:omeRawAlertInfo})