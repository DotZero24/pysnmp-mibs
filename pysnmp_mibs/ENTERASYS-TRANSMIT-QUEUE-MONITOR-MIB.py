_f='etsysTxqMonitorNotificationGroup'
_e='etsysTxqMonitorSettings'
_d='etsysTxqMonitorDisablePortNotification'
_c='etsysTxqMonitorIgnorePauseNotification'
_b='etsysTxqMonitorLoggingNotification'
_a='etsysTxqMonitorPortCapabilities'
_Z='etsysTxqMonitorPortReset'
_Y='etsysTxqMonitorPortOperationalStatus'
_X='etsysTxqMonitorPortTotalStalled'
_W='etsysTxqMonitorPortConsecutiveStalled'
_V='etsysTxqMonitorEnableState'
_U='etsysTxqMonitorTrapStatus'
_T='etsysTxqMonitorSampleInterval'
_S='etsysTxqMonitorMinRate'
_R='etsysTxqMonitorIgnorePauseTime'
_Q='etsysTxqMonitorDownTime'
_P='ignorePause'
_O='logging'
_N='enabled'
_M='TruthValue'
_L='ifIndex'
_K='etsysTxqMonitorDisablePortThreshold'
_J='etsysTxqMonitorIgnorePauseThreshold'
_I='etsysTxqMonitorLoggingThreshold'
_H='disabled'
_G='read-only'
_F='ifName'
_E='IF-MIB'
_D='read-write'
_C='Integer32'
_B='current'
_A='ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ifIndex,ifName=mibBuilder.importSymbols(_E,_L,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_M)
etsysTxqMonitorMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,99))
if mibBuilder.loadTexts:etsysTxqMonitorMIB.setRevisions(('2013-02-25 16:27',))
_EtsysTxqMonitorObjects_ObjectIdentity=ObjectIdentity
etsysTxqMonitorObjects=_EtsysTxqMonitorObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,99,1))
_EtsysTxqMonitorNotifications_ObjectIdentity=ObjectIdentity
etsysTxqMonitorNotifications=_EtsysTxqMonitorNotifications_ObjectIdentity((1,3,6,1,4,1,5624,1,2,99,1,0))
_EtsysTxqMonitor_ObjectIdentity=ObjectIdentity
etsysTxqMonitor=_EtsysTxqMonitor_ObjectIdentity((1,3,6,1,4,1,5624,1,2,99,1,1))
class _EtsysTxqMonitorDownTime_Type(Integer32):defaultValue=0
_EtsysTxqMonitorDownTime_Type.__name__=_C
_EtsysTxqMonitorDownTime_Object=MibScalar
etsysTxqMonitorDownTime=_EtsysTxqMonitorDownTime_Object((1,3,6,1,4,1,5624,1,2,99,1,1,1),_EtsysTxqMonitorDownTime_Type())
etsysTxqMonitorDownTime.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTxqMonitorDownTime.setStatus(_B)
class _EtsysTxqMonitorIgnorePauseTime_Type(Integer32):defaultValue=0
_EtsysTxqMonitorIgnorePauseTime_Type.__name__=_C
_EtsysTxqMonitorIgnorePauseTime_Object=MibScalar
etsysTxqMonitorIgnorePauseTime=_EtsysTxqMonitorIgnorePauseTime_Object((1,3,6,1,4,1,5624,1,2,99,1,1,2),_EtsysTxqMonitorIgnorePauseTime_Type())
etsysTxqMonitorIgnorePauseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTxqMonitorIgnorePauseTime.setStatus(_B)
class _EtsysTxqMonitorMinRate_Type(Integer32):defaultValue=1
_EtsysTxqMonitorMinRate_Type.__name__=_C
_EtsysTxqMonitorMinRate_Object=MibScalar
etsysTxqMonitorMinRate=_EtsysTxqMonitorMinRate_Object((1,3,6,1,4,1,5624,1,2,99,1,1,3),_EtsysTxqMonitorMinRate_Type())
etsysTxqMonitorMinRate.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTxqMonitorMinRate.setStatus(_B)
class _EtsysTxqMonitorSampleInterval_Type(Integer32):defaultValue=1
_EtsysTxqMonitorSampleInterval_Type.__name__=_C
_EtsysTxqMonitorSampleInterval_Object=MibScalar
etsysTxqMonitorSampleInterval=_EtsysTxqMonitorSampleInterval_Object((1,3,6,1,4,1,5624,1,2,99,1,1,4),_EtsysTxqMonitorSampleInterval_Type())
etsysTxqMonitorSampleInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTxqMonitorSampleInterval.setStatus(_B)
class _EtsysTxqMonitorTrapStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_H,2)))
_EtsysTxqMonitorTrapStatus_Type.__name__=_C
_EtsysTxqMonitorTrapStatus_Object=MibScalar
etsysTxqMonitorTrapStatus=_EtsysTxqMonitorTrapStatus_Object((1,3,6,1,4,1,5624,1,2,99,1,1,5),_EtsysTxqMonitorTrapStatus_Type())
etsysTxqMonitorTrapStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTxqMonitorTrapStatus.setStatus(_B)
class _EtsysTxqMonitorLoggingThreshold_Type(Integer32):defaultValue=2
_EtsysTxqMonitorLoggingThreshold_Type.__name__=_C
_EtsysTxqMonitorLoggingThreshold_Object=MibScalar
etsysTxqMonitorLoggingThreshold=_EtsysTxqMonitorLoggingThreshold_Object((1,3,6,1,4,1,5624,1,2,99,1,1,6),_EtsysTxqMonitorLoggingThreshold_Type())
etsysTxqMonitorLoggingThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTxqMonitorLoggingThreshold.setStatus(_B)
class _EtsysTxqMonitorIgnorePauseThreshold_Type(Integer32):defaultValue=5
_EtsysTxqMonitorIgnorePauseThreshold_Type.__name__=_C
_EtsysTxqMonitorIgnorePauseThreshold_Object=MibScalar
etsysTxqMonitorIgnorePauseThreshold=_EtsysTxqMonitorIgnorePauseThreshold_Object((1,3,6,1,4,1,5624,1,2,99,1,1,7),_EtsysTxqMonitorIgnorePauseThreshold_Type())
etsysTxqMonitorIgnorePauseThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTxqMonitorIgnorePauseThreshold.setStatus(_B)
class _EtsysTxqMonitorDisablePortThreshold_Type(Integer32):defaultValue=10
_EtsysTxqMonitorDisablePortThreshold_Type.__name__=_C
_EtsysTxqMonitorDisablePortThreshold_Object=MibScalar
etsysTxqMonitorDisablePortThreshold=_EtsysTxqMonitorDisablePortThreshold_Object((1,3,6,1,4,1,5624,1,2,99,1,1,8),_EtsysTxqMonitorDisablePortThreshold_Type())
etsysTxqMonitorDisablePortThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTxqMonitorDisablePortThreshold.setStatus(_B)
class _EtsysTxqMonitorEnableState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_H,2)))
_EtsysTxqMonitorEnableState_Type.__name__=_C
_EtsysTxqMonitorEnableState_Object=MibScalar
etsysTxqMonitorEnableState=_EtsysTxqMonitorEnableState_Object((1,3,6,1,4,1,5624,1,2,99,1,1,9),_EtsysTxqMonitorEnableState_Type())
etsysTxqMonitorEnableState.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTxqMonitorEnableState.setStatus(_B)
_EtsysTxqMonitorPort_ObjectIdentity=ObjectIdentity
etsysTxqMonitorPort=_EtsysTxqMonitorPort_ObjectIdentity((1,3,6,1,4,1,5624,1,2,99,1,2))
_EtsysTxqMonitorPortTable_Object=MibTable
etsysTxqMonitorPortTable=_EtsysTxqMonitorPortTable_Object((1,3,6,1,4,1,5624,1,2,99,1,2,1))
if mibBuilder.loadTexts:etsysTxqMonitorPortTable.setStatus(_B)
_EtsysTxqMonitorPortEntry_Object=MibTableRow
etsysTxqMonitorPortEntry=_EtsysTxqMonitorPortEntry_Object((1,3,6,1,4,1,5624,1,2,99,1,2,1,1))
etsysTxqMonitorPortEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:etsysTxqMonitorPortEntry.setStatus(_B)
_EtsysTxqMonitorPortConsecutiveStalled_Type=Counter64
_EtsysTxqMonitorPortConsecutiveStalled_Object=MibTableColumn
etsysTxqMonitorPortConsecutiveStalled=_EtsysTxqMonitorPortConsecutiveStalled_Object((1,3,6,1,4,1,5624,1,2,99,1,2,1,1,1),_EtsysTxqMonitorPortConsecutiveStalled_Type())
etsysTxqMonitorPortConsecutiveStalled.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysTxqMonitorPortConsecutiveStalled.setStatus(_B)
_EtsysTxqMonitorPortTotalStalled_Type=Counter64
_EtsysTxqMonitorPortTotalStalled_Object=MibTableColumn
etsysTxqMonitorPortTotalStalled=_EtsysTxqMonitorPortTotalStalled_Object((1,3,6,1,4,1,5624,1,2,99,1,2,1,1,2),_EtsysTxqMonitorPortTotalStalled_Type())
etsysTxqMonitorPortTotalStalled.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysTxqMonitorPortTotalStalled.setStatus(_B)
class _EtsysTxqMonitorPortOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),('normal',2),(_O,3),(_P,4),('down',5)))
_EtsysTxqMonitorPortOperationalStatus_Type.__name__=_C
_EtsysTxqMonitorPortOperationalStatus_Object=MibTableColumn
etsysTxqMonitorPortOperationalStatus=_EtsysTxqMonitorPortOperationalStatus_Object((1,3,6,1,4,1,5624,1,2,99,1,2,1,1,3),_EtsysTxqMonitorPortOperationalStatus_Type())
etsysTxqMonitorPortOperationalStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysTxqMonitorPortOperationalStatus.setStatus(_B)
class _EtsysTxqMonitorPortReset_Type(TruthValue):defaultValue=2
_EtsysTxqMonitorPortReset_Type.__name__=_M
_EtsysTxqMonitorPortReset_Object=MibTableColumn
etsysTxqMonitorPortReset=_EtsysTxqMonitorPortReset_Object((1,3,6,1,4,1,5624,1,2,99,1,2,1,1,4),_EtsysTxqMonitorPortReset_Type())
etsysTxqMonitorPortReset.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTxqMonitorPortReset.setStatus(_B)
class _EtsysTxqMonitorPortCapabilities_Type(Bits):namedValues=NamedValues(*((_O,0),(_P,1),('down',2)))
_EtsysTxqMonitorPortCapabilities_Type.__name__='Bits'
_EtsysTxqMonitorPortCapabilities_Object=MibTableColumn
etsysTxqMonitorPortCapabilities=_EtsysTxqMonitorPortCapabilities_Object((1,3,6,1,4,1,5624,1,2,99,1,2,1,1,5),_EtsysTxqMonitorPortCapabilities_Type())
etsysTxqMonitorPortCapabilities.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysTxqMonitorPortCapabilities.setStatus(_B)
_EtsysTxqMonitorConformance_ObjectIdentity=ObjectIdentity
etsysTxqMonitorConformance=_EtsysTxqMonitorConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,99,2))
_EtsysTxqMonitorGroups_ObjectIdentity=ObjectIdentity
etsysTxqMonitorGroups=_EtsysTxqMonitorGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,99,2,1))
_EtsysTxqMonitorCompliances_ObjectIdentity=ObjectIdentity
etsysTxqMonitorCompliances=_EtsysTxqMonitorCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,99,2,2))
etsysTxqMonitorSettings=ObjectGroup((1,3,6,1,4,1,5624,1,2,99,2,1,1))
etsysTxqMonitorSettings.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_I),(_A,_J),(_A,_K),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:etsysTxqMonitorSettings.setStatus(_B)
etsysTxqMonitorLoggingNotification=NotificationType((1,3,6,1,4,1,5624,1,2,99,1,0,1))
etsysTxqMonitorLoggingNotification.setObjects(*((_E,_F),(_A,_I)))
if mibBuilder.loadTexts:etsysTxqMonitorLoggingNotification.setStatus(_B)
etsysTxqMonitorIgnorePauseNotification=NotificationType((1,3,6,1,4,1,5624,1,2,99,1,0,2))
etsysTxqMonitorIgnorePauseNotification.setObjects(*((_E,_F),(_A,_J)))
if mibBuilder.loadTexts:etsysTxqMonitorIgnorePauseNotification.setStatus(_B)
etsysTxqMonitorDisablePortNotification=NotificationType((1,3,6,1,4,1,5624,1,2,99,1,0,3))
etsysTxqMonitorDisablePortNotification.setObjects(*((_E,_F),(_A,_K)))
if mibBuilder.loadTexts:etsysTxqMonitorDisablePortNotification.setStatus(_B)
etsysTxqMonitorNotificationGroup=NotificationGroup((1,3,6,1,4,1,5624,1,2,99,2,1,2))
etsysTxqMonitorNotificationGroup.setObjects(*((_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:etsysTxqMonitorNotificationGroup.setStatus(_B)
etsysTxqMonitorComplianceGroup=ModuleCompliance((1,3,6,1,4,1,5624,1,2,99,2,2,1))
etsysTxqMonitorComplianceGroup.setObjects(*((_A,_e),(_A,_f)))
if mibBuilder.loadTexts:etsysTxqMonitorComplianceGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'etsysTxqMonitorMIB':etsysTxqMonitorMIB,'etsysTxqMonitorObjects':etsysTxqMonitorObjects,'etsysTxqMonitorNotifications':etsysTxqMonitorNotifications,_b:etsysTxqMonitorLoggingNotification,_c:etsysTxqMonitorIgnorePauseNotification,_d:etsysTxqMonitorDisablePortNotification,'etsysTxqMonitor':etsysTxqMonitor,_Q:etsysTxqMonitorDownTime,_R:etsysTxqMonitorIgnorePauseTime,_S:etsysTxqMonitorMinRate,_T:etsysTxqMonitorSampleInterval,_U:etsysTxqMonitorTrapStatus,_I:etsysTxqMonitorLoggingThreshold,_J:etsysTxqMonitorIgnorePauseThreshold,_K:etsysTxqMonitorDisablePortThreshold,_V:etsysTxqMonitorEnableState,'etsysTxqMonitorPort':etsysTxqMonitorPort,'etsysTxqMonitorPortTable':etsysTxqMonitorPortTable,'etsysTxqMonitorPortEntry':etsysTxqMonitorPortEntry,_W:etsysTxqMonitorPortConsecutiveStalled,_X:etsysTxqMonitorPortTotalStalled,_Y:etsysTxqMonitorPortOperationalStatus,_Z:etsysTxqMonitorPortReset,_a:etsysTxqMonitorPortCapabilities,'etsysTxqMonitorConformance':etsysTxqMonitorConformance,'etsysTxqMonitorGroups':etsysTxqMonitorGroups,_e:etsysTxqMonitorSettings,_f:etsysTxqMonitorNotificationGroup,'etsysTxqMonitorCompliances':etsysTxqMonitorCompliances,'etsysTxqMonitorComplianceGroup':etsysTxqMonitorComplianceGroup})