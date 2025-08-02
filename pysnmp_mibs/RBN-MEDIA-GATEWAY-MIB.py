_M='rbnMGLinkNotifyGroup'
_L='rbnMGNotifyObjectGroup'
_K='rbnH248LinkStatusAlarm'
_J='rbnMGEventInformation'
_I='rbnMGEventProbableCause'
_H='rbnMGEventType'
_G='rbnMGEventSender'
_F='rbnMGEventSeverity'
_E='rbnMGEventDateAndTime'
_D='SnmpAdminString'
_C='accessible-for-notify'
_B='current'
_A='RBN-MEDIA-GATEWAY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAItuEventType,IANAItuProbableCause=mibBuilder.importSymbols('IANA-ITU-ALARM-TC-MIB','IANAItuEventType','IANAItuProbableCause')
ItuPerceivedSeverity,=mibBuilder.importSymbols('ITU-ALARM-TC-MIB','ItuPerceivedSeverity')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
rbnMediaGatewayMib=ModuleIdentity((1,3,6,1,4,1,2352,2,52))
if mibBuilder.loadTexts:rbnMediaGatewayMib.setRevisions(('2010-04-19 00:00','2009-09-30 00:00'))
_RbnMediaGatewayNotifications_ObjectIdentity=ObjectIdentity
rbnMediaGatewayNotifications=_RbnMediaGatewayNotifications_ObjectIdentity((1,3,6,1,4,1,2352,2,52,0))
_RbnMediaGatewayObjects_ObjectIdentity=ObjectIdentity
rbnMediaGatewayObjects=_RbnMediaGatewayObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,52,1))
_RbnMediaGatewayNotify_ObjectIdentity=ObjectIdentity
rbnMediaGatewayNotify=_RbnMediaGatewayNotify_ObjectIdentity((1,3,6,1,4,1,2352,2,52,1,1))
_RbnMGEventDateAndTime_Type=DateAndTime
_RbnMGEventDateAndTime_Object=MibScalar
rbnMGEventDateAndTime=_RbnMGEventDateAndTime_Object((1,3,6,1,4,1,2352,2,52,1,1,1),_RbnMGEventDateAndTime_Type())
rbnMGEventDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMGEventDateAndTime.setStatus(_B)
_RbnMGEventSeverity_Type=ItuPerceivedSeverity
_RbnMGEventSeverity_Object=MibScalar
rbnMGEventSeverity=_RbnMGEventSeverity_Object((1,3,6,1,4,1,2352,2,52,1,1,2),_RbnMGEventSeverity_Type())
rbnMGEventSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMGEventSeverity.setStatus(_B)
class _RbnMGEventSender_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RbnMGEventSender_Type.__name__=_D
_RbnMGEventSender_Object=MibScalar
rbnMGEventSender=_RbnMGEventSender_Object((1,3,6,1,4,1,2352,2,52,1,1,3),_RbnMGEventSender_Type())
rbnMGEventSender.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMGEventSender.setStatus(_B)
_RbnMGEventType_Type=IANAItuEventType
_RbnMGEventType_Object=MibScalar
rbnMGEventType=_RbnMGEventType_Object((1,3,6,1,4,1,2352,2,52,1,1,4),_RbnMGEventType_Type())
rbnMGEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMGEventType.setStatus(_B)
_RbnMGEventProbableCause_Type=IANAItuProbableCause
_RbnMGEventProbableCause_Object=MibScalar
rbnMGEventProbableCause=_RbnMGEventProbableCause_Object((1,3,6,1,4,1,2352,2,52,1,1,5),_RbnMGEventProbableCause_Type())
rbnMGEventProbableCause.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMGEventProbableCause.setStatus(_B)
class _RbnMGEventInformation_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_RbnMGEventInformation_Type.__name__=_D
_RbnMGEventInformation_Object=MibScalar
rbnMGEventInformation=_RbnMGEventInformation_Object((1,3,6,1,4,1,2352,2,52,1,1,6),_RbnMGEventInformation_Type())
rbnMGEventInformation.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMGEventInformation.setStatus(_B)
_RbnMediaGatewayConformance_ObjectIdentity=ObjectIdentity
rbnMediaGatewayConformance=_RbnMediaGatewayConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,52,2))
_RbnMediaGatewayCompliances_ObjectIdentity=ObjectIdentity
rbnMediaGatewayCompliances=_RbnMediaGatewayCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,52,2,1))
_RbnMediaGatewayGroups_ObjectIdentity=ObjectIdentity
rbnMediaGatewayGroups=_RbnMediaGatewayGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,52,2,2))
rbnMGNotifyObjectGroup=ObjectGroup((1,3,6,1,4,1,2352,2,52,2,2,1))
rbnMGNotifyObjectGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:rbnMGNotifyObjectGroup.setStatus(_B)
rbnH248LinkStatusAlarm=NotificationType((1,3,6,1,4,1,2352,2,52,0,1))
rbnH248LinkStatusAlarm.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:rbnH248LinkStatusAlarm.setStatus(_B)
rbnMGLinkNotifyGroup=NotificationGroup((1,3,6,1,4,1,2352,2,52,2,2,2))
rbnMGLinkNotifyGroup.setObjects((_A,_K))
if mibBuilder.loadTexts:rbnMGLinkNotifyGroup.setStatus(_B)
rbnMGCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,52,2,1,1))
rbnMGCompliance.setObjects(*((_A,_L),(_A,_M)))
if mibBuilder.loadTexts:rbnMGCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'rbnMediaGatewayMib':rbnMediaGatewayMib,'rbnMediaGatewayNotifications':rbnMediaGatewayNotifications,_K:rbnH248LinkStatusAlarm,'rbnMediaGatewayObjects':rbnMediaGatewayObjects,'rbnMediaGatewayNotify':rbnMediaGatewayNotify,_E:rbnMGEventDateAndTime,_F:rbnMGEventSeverity,_G:rbnMGEventSender,_H:rbnMGEventType,_I:rbnMGEventProbableCause,_J:rbnMGEventInformation,'rbnMediaGatewayConformance':rbnMediaGatewayConformance,'rbnMediaGatewayCompliances':rbnMediaGatewayCompliances,'rbnMGCompliance':rbnMGCompliance,'rbnMediaGatewayGroups':rbnMediaGatewayGroups,_L:rbnMGNotifyObjectGroup,_M:rbnMGLinkNotifyGroup})