_J='alertGroup'
_I='alertDescription'
_H='alertTimeStamp'
_G='alertSeverity'
_F='alertEffect'
_E='alertSource'
_D='DisplayString'
_C='read-only'
_B='F5-ALERT-DEF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
f5Compliance,platform=mibBuilder.importSymbols('F5-COMMON-SMI-MIB','f5Compliance','platform')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
f5Alerts=ModuleIdentity((1,3,6,1,4,1,12276,1,1))
if mibBuilder.loadTexts:f5Alerts.setRevisions(('2019-08-01 09:41',))
class F5Severity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('info',6),('debug',7),('na',8)))
class F5CondEffect(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,9999)));namedValues=NamedValues(*(('clear',0),('assert',1),('event',2),('other',9999)))
_F5AlertObjects_ObjectIdentity=ObjectIdentity
f5AlertObjects=_F5AlertObjects_ObjectIdentity((1,3,6,1,4,1,12276,1,1,0))
_F5AlertNotificationObject_ObjectIdentity=ObjectIdentity
f5AlertNotificationObject=_F5AlertNotificationObject_ObjectIdentity((1,3,6,1,4,1,12276,1,1,0,1))
class _AlertSource_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AlertSource_Type.__name__=_D
_AlertSource_Object=MibScalar
alertSource=_AlertSource_Object((1,3,6,1,4,1,12276,1,1,0,1,1),_AlertSource_Type())
alertSource.setMaxAccess(_C)
if mibBuilder.loadTexts:alertSource.setStatus(_A)
_AlertEffect_Type=F5CondEffect
_AlertEffect_Object=MibScalar
alertEffect=_AlertEffect_Object((1,3,6,1,4,1,12276,1,1,0,1,2),_AlertEffect_Type())
alertEffect.setMaxAccess(_C)
if mibBuilder.loadTexts:alertEffect.setStatus(_A)
_AlertSeverity_Type=F5Severity
_AlertSeverity_Object=MibScalar
alertSeverity=_AlertSeverity_Object((1,3,6,1,4,1,12276,1,1,0,1,3),_AlertSeverity_Type())
alertSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:alertSeverity.setStatus(_A)
class _AlertTimeStamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_AlertTimeStamp_Type.__name__=_D
_AlertTimeStamp_Object=MibScalar
alertTimeStamp=_AlertTimeStamp_Object((1,3,6,1,4,1,12276,1,1,0,1,4),_AlertTimeStamp_Type())
alertTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:alertTimeStamp.setStatus(_A)
class _AlertDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_AlertDescription_Type.__name__=_D
_AlertDescription_Object=MibScalar
alertDescription=_AlertDescription_Object((1,3,6,1,4,1,12276,1,1,0,1,5),_AlertDescription_Type())
alertDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:alertDescription.setStatus(_A)
_F5AlertNotificationObjectGroup_ObjectIdentity=ObjectIdentity
f5AlertNotificationObjectGroup=_F5AlertNotificationObjectGroup_ObjectIdentity((1,3,6,1,4,1,12276,1,1,0,2))
_F5AlertNotificationGroup_ObjectIdentity=ObjectIdentity
f5AlertNotificationGroup=_F5AlertNotificationGroup_ObjectIdentity((1,3,6,1,4,1,12276,1,1,0,3))
alertGroup=ObjectGroup((1,3,6,1,4,1,12276,1,1,0,2,1))
alertGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:alertGroup.setStatus(_A)
f5AlertGroupCompliance=ModuleCompliance((1,3,6,1,4,1,12276,2,1))
f5AlertGroupCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:f5AlertGroupCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'F5Severity':F5Severity,'F5CondEffect':F5CondEffect,'f5Alerts':f5Alerts,'f5AlertObjects':f5AlertObjects,'f5AlertNotificationObject':f5AlertNotificationObject,_E:alertSource,_F:alertEffect,_G:alertSeverity,_H:alertTimeStamp,_I:alertDescription,'f5AlertNotificationObjectGroup':f5AlertNotificationObjectGroup,_J:alertGroup,'f5AlertNotificationGroup':f5AlertNotificationGroup,'f5AlertGroupCompliance':f5AlertGroupCompliance})