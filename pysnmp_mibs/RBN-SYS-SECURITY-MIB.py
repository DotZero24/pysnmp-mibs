_R='rbnSysSecNotificationGroup'
_Q='rbnSysSecNotifyObjectsGroup'
_P='rbnMaliciousPktGroup'
_O='rbnMaliciousPktThresholdLowExceeded'
_N='rbnMaliciousPktThresholdHiExceeded'
_M='rbnMaliciousPktsDelta'
_L='rbnMaliciousPktsCounter'
_K='rbnMaliciousPktsThresholdLow'
_J='rbnMaliciousPktsThresholdHi'
_I='rbnMeasurementInterval'
_H='rbnSysSecNotifyEnable'
_G='accessible-for-notify'
_F='Gauge32'
_E='rbnThresholdNotifyTime'
_D='Packets'
_C='read-write'
_B='current'
_A='RBN-SYS-SECURITY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
rbnModules,=mibBuilder.importSymbols('RBN-SMI','rbnModules')
RbnUnsigned64,=mibBuilder.importSymbols('RBN-TC','RbnUnsigned64')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_F,'Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
rbnSysSecurityMib=ModuleIdentity((1,3,6,1,4,1,2352,5,54))
if mibBuilder.loadTexts:rbnSysSecurityMib.setRevisions(('2009-11-09 18:00',))
_RbnSysSecNotifications_ObjectIdentity=ObjectIdentity
rbnSysSecNotifications=_RbnSysSecNotifications_ObjectIdentity((1,3,6,1,4,1,2352,5,54,0))
_RbnSysSecObjects_ObjectIdentity=ObjectIdentity
rbnSysSecObjects=_RbnSysSecObjects_ObjectIdentity((1,3,6,1,4,1,2352,5,54,1))
_RbnSysSecThresholdObjects_ObjectIdentity=ObjectIdentity
rbnSysSecThresholdObjects=_RbnSysSecThresholdObjects_ObjectIdentity((1,3,6,1,4,1,2352,5,54,1,1))
class _RbnSysSecNotifyEnable_Type(Bits):defaultBinValue='0';namedValues=NamedValues(('maliciousPkt',0))
_RbnSysSecNotifyEnable_Type.__name__='Bits'
_RbnSysSecNotifyEnable_Object=MibScalar
rbnSysSecNotifyEnable=_RbnSysSecNotifyEnable_Object((1,3,6,1,4,1,2352,5,54,1,1,1),_RbnSysSecNotifyEnable_Type())
rbnSysSecNotifyEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnSysSecNotifyEnable.setStatus(_B)
class _RbnMeasurementInterval_Type(Gauge32):defaultValue=60;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_RbnMeasurementInterval_Type.__name__=_F
_RbnMeasurementInterval_Object=MibScalar
rbnMeasurementInterval=_RbnMeasurementInterval_Object((1,3,6,1,4,1,2352,5,54,1,1,2),_RbnMeasurementInterval_Type())
rbnMeasurementInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMeasurementInterval.setStatus(_B)
if mibBuilder.loadTexts:rbnMeasurementInterval.setUnits('seconds')
_RbnMaliciousPktsThresholdHi_Type=RbnUnsigned64
_RbnMaliciousPktsThresholdHi_Object=MibScalar
rbnMaliciousPktsThresholdHi=_RbnMaliciousPktsThresholdHi_Object((1,3,6,1,4,1,2352,5,54,1,1,3),_RbnMaliciousPktsThresholdHi_Type())
rbnMaliciousPktsThresholdHi.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMaliciousPktsThresholdHi.setStatus(_B)
if mibBuilder.loadTexts:rbnMaliciousPktsThresholdHi.setUnits(_D)
_RbnMaliciousPktsThresholdLow_Type=RbnUnsigned64
_RbnMaliciousPktsThresholdLow_Object=MibScalar
rbnMaliciousPktsThresholdLow=_RbnMaliciousPktsThresholdLow_Object((1,3,6,1,4,1,2352,5,54,1,1,4),_RbnMaliciousPktsThresholdLow_Type())
rbnMaliciousPktsThresholdLow.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMaliciousPktsThresholdLow.setStatus(_B)
if mibBuilder.loadTexts:rbnMaliciousPktsThresholdLow.setUnits(_D)
_RbnSysSecStatsObjects_ObjectIdentity=ObjectIdentity
rbnSysSecStatsObjects=_RbnSysSecStatsObjects_ObjectIdentity((1,3,6,1,4,1,2352,5,54,1,2))
_RbnMaliciousPktsCounter_Type=Counter64
_RbnMaliciousPktsCounter_Object=MibScalar
rbnMaliciousPktsCounter=_RbnMaliciousPktsCounter_Object((1,3,6,1,4,1,2352,5,54,1,2,1),_RbnMaliciousPktsCounter_Type())
rbnMaliciousPktsCounter.setMaxAccess('read-only')
if mibBuilder.loadTexts:rbnMaliciousPktsCounter.setStatus(_B)
if mibBuilder.loadTexts:rbnMaliciousPktsCounter.setUnits(_D)
_RbnMaliciousPktsDelta_Type=CounterBasedGauge64
_RbnMaliciousPktsDelta_Object=MibScalar
rbnMaliciousPktsDelta=_RbnMaliciousPktsDelta_Object((1,3,6,1,4,1,2352,5,54,1,2,2),_RbnMaliciousPktsDelta_Type())
rbnMaliciousPktsDelta.setMaxAccess(_G)
if mibBuilder.loadTexts:rbnMaliciousPktsDelta.setStatus(_B)
if mibBuilder.loadTexts:rbnMaliciousPktsDelta.setUnits('packets')
_RbnSysSecNotifyObjects_ObjectIdentity=ObjectIdentity
rbnSysSecNotifyObjects=_RbnSysSecNotifyObjects_ObjectIdentity((1,3,6,1,4,1,2352,5,54,1,4))
_RbnThresholdNotifyTime_Type=DateAndTime
_RbnThresholdNotifyTime_Object=MibScalar
rbnThresholdNotifyTime=_RbnThresholdNotifyTime_Object((1,3,6,1,4,1,2352,5,54,1,4,1),_RbnThresholdNotifyTime_Type())
rbnThresholdNotifyTime.setMaxAccess(_G)
if mibBuilder.loadTexts:rbnThresholdNotifyTime.setStatus(_B)
_RbnSysSecConformance_ObjectIdentity=ObjectIdentity
rbnSysSecConformance=_RbnSysSecConformance_ObjectIdentity((1,3,6,1,4,1,2352,5,54,2))
_RbnSysSecCompliances_ObjectIdentity=ObjectIdentity
rbnSysSecCompliances=_RbnSysSecCompliances_ObjectIdentity((1,3,6,1,4,1,2352,5,54,2,1))
_RbnSysSecGroups_ObjectIdentity=ObjectIdentity
rbnSysSecGroups=_RbnSysSecGroups_ObjectIdentity((1,3,6,1,4,1,2352,5,54,2,2))
rbnMaliciousPktGroup=ObjectGroup((1,3,6,1,4,1,2352,5,54,2,2,1))
rbnMaliciousPktGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:rbnMaliciousPktGroup.setStatus(_B)
rbnSysSecNotifyObjectsGroup=ObjectGroup((1,3,6,1,4,1,2352,5,54,2,2,4))
rbnSysSecNotifyObjectsGroup.setObjects(*((_A,_M),(_A,_E)))
if mibBuilder.loadTexts:rbnSysSecNotifyObjectsGroup.setStatus(_B)
rbnMaliciousPktThresholdHiExceeded=NotificationType((1,3,6,1,4,1,2352,5,54,0,1))
if mibBuilder.loadTexts:rbnMaliciousPktThresholdHiExceeded.setStatus(_B)
rbnMaliciousPktThresholdLowExceeded=NotificationType((1,3,6,1,4,1,2352,5,54,0,2))
rbnMaliciousPktThresholdLowExceeded.setObjects((_A,_E))
if mibBuilder.loadTexts:rbnMaliciousPktThresholdLowExceeded.setStatus(_B)
rbnSysSecNotificationGroup=NotificationGroup((1,3,6,1,4,1,2352,5,54,2,2,5))
rbnSysSecNotificationGroup.setObjects(*((_A,_N),(_A,_O)))
if mibBuilder.loadTexts:rbnSysSecNotificationGroup.setStatus(_B)
rbnSysSecCompliance=ModuleCompliance((1,3,6,1,4,1,2352,5,54,2,1,1))
rbnSysSecCompliance.setObjects(*((_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:rbnSysSecCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'rbnSysSecurityMib':rbnSysSecurityMib,'rbnSysSecNotifications':rbnSysSecNotifications,_N:rbnMaliciousPktThresholdHiExceeded,_O:rbnMaliciousPktThresholdLowExceeded,'rbnSysSecObjects':rbnSysSecObjects,'rbnSysSecThresholdObjects':rbnSysSecThresholdObjects,_H:rbnSysSecNotifyEnable,_I:rbnMeasurementInterval,_J:rbnMaliciousPktsThresholdHi,_K:rbnMaliciousPktsThresholdLow,'rbnSysSecStatsObjects':rbnSysSecStatsObjects,_L:rbnMaliciousPktsCounter,_M:rbnMaliciousPktsDelta,'rbnSysSecNotifyObjects':rbnSysSecNotifyObjects,_E:rbnThresholdNotifyTime,'rbnSysSecConformance':rbnSysSecConformance,'rbnSysSecCompliances':rbnSysSecCompliances,'rbnSysSecCompliance':rbnSysSecCompliance,'rbnSysSecGroups':rbnSysSecGroups,_P:rbnMaliciousPktGroup,_Q:rbnSysSecNotifyObjectsGroup,_R:rbnSysSecNotificationGroup})