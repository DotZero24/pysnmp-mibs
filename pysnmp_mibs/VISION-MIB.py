_O='alertSourceDeviceIp'
_N='alertSourceDeviceName'
_M='alertTimeMillis'
_L='alertTimeString'
_K='alertCategory'
_J='alertModule'
_I='alertSeverity'
_H='alertUser'
_G='alertMessage'
_F='alertId'
_E='NotificationType'
_D='DisplayString'
_C='current'
_B='read-only'
_A='VISION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rndApplications,=mibBuilder.importSymbols('RADWARE-MIB','rndApplications')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_E,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_E,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
_Managment_ObjectIdentity=ObjectIdentity
managment=_Managment_ObjectIdentity((1,3,6,1,4,1,89,35,10))
_Alerts_ObjectIdentity=ObjectIdentity
alerts=_Alerts_ObjectIdentity((1,3,6,1,4,1,89,35,10,1))
_AlertId_Type=Integer32
_AlertId_Object=MibScalar
alertId=_AlertId_Object((1,3,6,1,4,1,89,35,10,1,1),_AlertId_Type())
alertId.setMaxAccess(_B)
if mibBuilder.loadTexts:alertId.setStatus(_C)
_AlertMessage_Type=DisplayString
_AlertMessage_Object=MibScalar
alertMessage=_AlertMessage_Object((1,3,6,1,4,1,89,35,10,1,2),_AlertMessage_Type())
alertMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:alertMessage.setStatus(_C)
class _AlertUser_Type(DisplayString):defaultValue=OctetString('APSolute_Vision')
_AlertUser_Type.__name__=_D
_AlertUser_Object=MibScalar
alertUser=_AlertUser_Object((1,3,6,1,4,1,89,35,10,1,3),_AlertUser_Type())
alertUser.setMaxAccess(_B)
if mibBuilder.loadTexts:alertUser.setStatus(_C)
_AlertSeverity_Type=DisplayString
_AlertSeverity_Object=MibScalar
alertSeverity=_AlertSeverity_Object((1,3,6,1,4,1,89,35,10,1,4),_AlertSeverity_Type())
alertSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:alertSeverity.setStatus(_C)
_AlertModule_Type=DisplayString
_AlertModule_Object=MibScalar
alertModule=_AlertModule_Object((1,3,6,1,4,1,89,35,10,1,5),_AlertModule_Type())
alertModule.setMaxAccess(_B)
if mibBuilder.loadTexts:alertModule.setStatus(_C)
_AlertCategory_Type=DisplayString
_AlertCategory_Object=MibScalar
alertCategory=_AlertCategory_Object((1,3,6,1,4,1,89,35,10,1,6),_AlertCategory_Type())
alertCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:alertCategory.setStatus(_C)
_AlertTimeString_Type=DisplayString
_AlertTimeString_Object=MibScalar
alertTimeString=_AlertTimeString_Object((1,3,6,1,4,1,89,35,10,1,7),_AlertTimeString_Type())
alertTimeString.setMaxAccess(_B)
if mibBuilder.loadTexts:alertTimeString.setStatus(_C)
_AlertTimeMillis_Type=Counter64
_AlertTimeMillis_Object=MibScalar
alertTimeMillis=_AlertTimeMillis_Object((1,3,6,1,4,1,89,35,10,1,8),_AlertTimeMillis_Type())
alertTimeMillis.setMaxAccess(_B)
if mibBuilder.loadTexts:alertTimeMillis.setStatus(_C)
class _AlertSourceDeviceName_Type(DisplayString):defaultValue=OctetString('')
_AlertSourceDeviceName_Type.__name__=_D
_AlertSourceDeviceName_Object=MibScalar
alertSourceDeviceName=_AlertSourceDeviceName_Object((1,3,6,1,4,1,89,35,10,1,9),_AlertSourceDeviceName_Type())
alertSourceDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:alertSourceDeviceName.setStatus(_C)
class _AlertSourceDeviceIp_Type(DisplayString):defaultValue=OctetString('')
_AlertSourceDeviceIp_Type.__name__=_D
_AlertSourceDeviceIp_Object=MibScalar
alertSourceDeviceIp=_AlertSourceDeviceIp_Object((1,3,6,1,4,1,89,35,10,1,10),_AlertSourceDeviceIp_Type())
alertSourceDeviceIp.setMaxAccess(_B)
if mibBuilder.loadTexts:alertSourceDeviceIp.setStatus(_C)
alertTrap=NotificationType((1,3,6,1,4,1,89,35,10,1,0,200))
alertTrap.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:alertTrap.setStatus('')
mibBuilder.exportSymbols(_A,**{'managment':managment,'alerts':alerts,'alertTrap':alertTrap,_F:alertId,_G:alertMessage,_H:alertUser,_I:alertSeverity,_J:alertModule,_K:alertCategory,_L:alertTimeString,_M:alertTimeMillis,_N:alertSourceDeviceName,_O:alertSourceDeviceIp})