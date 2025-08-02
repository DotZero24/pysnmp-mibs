_J='nnqosSLANotification'
_I='nnqosSlaThresholdValue2'
_H='nnqosSlaThresholdValue1'
_G='nnqosSlaEffectType'
_F='nnqosSlaThresholdType'
_E='nnqosSlaIndex'
_D='Integer32'
_C='accessible-for-notify'
_B='QOSSLA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntEnterpriseDataTasmanMgmt,=mibBuilder.importSymbols('NT-ENTERPRISE-DATA-MIB','ntEnterpriseDataTasmanMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
nnqosSLAMib=ModuleIdentity((1,3,6,1,4,1,562,73,1,1,1,24))
if mibBuilder.loadTexts:nnqosSLAMib.setRevisions(('1900-08-18 00:00',))
_NnqosSLANotifications_ObjectIdentity=ObjectIdentity
nnqosSLANotifications=_NnqosSLANotifications_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,24,1))
_NnqosSLATraps_ObjectIdentity=ObjectIdentity
nnqosSLATraps=_NnqosSLATraps_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,24,1,0))
_NnqosSLANotificationsVars_ObjectIdentity=ObjectIdentity
nnqosSLANotificationsVars=_NnqosSLANotificationsVars_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,24,2))
class _NnqosSlaIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_NnqosSlaIndex_Type.__name__=_D
_NnqosSlaIndex_Object=MibScalar
nnqosSlaIndex=_NnqosSlaIndex_Object((1,3,6,1,4,1,562,73,1,1,1,24,2,1),_NnqosSlaIndex_Type())
nnqosSlaIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nnqosSlaIndex.setStatus(_A)
class _NnqosSlaThresholdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('average',1),('immediate',2),('consecutive',3),('xofy',4)))
_NnqosSlaThresholdType_Type.__name__=_D
_NnqosSlaThresholdType_Object=MibScalar
nnqosSlaThresholdType=_NnqosSlaThresholdType_Object((1,3,6,1,4,1,562,73,1,1,1,24,2,2),_NnqosSlaThresholdType_Type())
nnqosSlaThresholdType.setMaxAccess(_C)
if mibBuilder.loadTexts:nnqosSlaThresholdType.setStatus(_A)
class _NnqosSlaEffectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('jitterAvg',1),('jitterAvgSrcDest',2),('jitterAvgDestSrc',3),('jitterMaxPosSrcDest',4),('jitterMaxPosDestSrc',5),('jitterMaxNegSrcDest',6),('jitterMaxNegDestSrc',7),('delayAvg',8),('delayAvgSrcDest',9),('delayAvgDestSrc',10),('delayMaxSrcDest',11),('delayMaxDestSrc',12),('packetLoss',13),('packetOutOfOrder',14),('packetLateArrival',15),('responseTime',16),('timeout',17)))
_NnqosSlaEffectType_Type.__name__=_D
_NnqosSlaEffectType_Object=MibScalar
nnqosSlaEffectType=_NnqosSlaEffectType_Object((1,3,6,1,4,1,562,73,1,1,1,24,2,3),_NnqosSlaEffectType_Type())
nnqosSlaEffectType.setMaxAccess(_C)
if mibBuilder.loadTexts:nnqosSlaEffectType.setStatus(_A)
_NnqosSlaThresholdValue1_Type=Integer32
_NnqosSlaThresholdValue1_Object=MibScalar
nnqosSlaThresholdValue1=_NnqosSlaThresholdValue1_Object((1,3,6,1,4,1,562,73,1,1,1,24,2,4),_NnqosSlaThresholdValue1_Type())
nnqosSlaThresholdValue1.setMaxAccess(_C)
if mibBuilder.loadTexts:nnqosSlaThresholdValue1.setStatus(_A)
_NnqosSlaThresholdValue2_Type=Integer32
_NnqosSlaThresholdValue2_Object=MibScalar
nnqosSlaThresholdValue2=_NnqosSlaThresholdValue2_Object((1,3,6,1,4,1,562,73,1,1,1,24,2,5),_NnqosSlaThresholdValue2_Type())
nnqosSlaThresholdValue2.setMaxAccess(_C)
if mibBuilder.loadTexts:nnqosSlaThresholdValue2.setStatus(_A)
nnqosSLANotification=NotificationType((1,3,6,1,4,1,562,73,1,1,1,24,1,0,1))
nnqosSLANotification.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:nnqosSLANotification.setStatus(_A)
nnqosNotificationGroup=NotificationGroup((1,3,6,1,4,1,562,73,1,1,1,24,3))
nnqosNotificationGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:nnqosNotificationGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'nnqosSLAMib':nnqosSLAMib,'nnqosSLANotifications':nnqosSLANotifications,'nnqosSLATraps':nnqosSLATraps,_J:nnqosSLANotification,'nnqosSLANotificationsVars':nnqosSLANotificationsVars,_E:nnqosSlaIndex,_F:nnqosSlaThresholdType,_G:nnqosSlaEffectType,_H:nnqosSlaThresholdValue1,_I:nnqosSlaThresholdValue2,'nnqosNotificationGroup':nnqosNotificationGroup})