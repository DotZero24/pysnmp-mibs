_Q='cIfMonNotifEventGroup'
_P='cIfMonNotifObjectGroup'
_O='cIfMonNotifEvent'
_N='cIfMonNotifLastChange'
_M='cIfMonNotifInterval'
_L='cIfMonNotifThreshold'
_K='cIfMonNotifValue'
_J='cIfMonNotifCause'
_I='cIfMonNotifSeverity'
_H='cIfMonNotifCount'
_G='Integer32'
_F='ifIndex'
_E='IF-MIB'
_D='Unsigned32'
_C='read-only'
_B='current'
_A='CISCO-IF-MONITOR-NOTIF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
ciscoIfMonitorNotifMIB=ModuleIdentity((1,3,6,1,4,1,9,10,999))
if mibBuilder.loadTexts:ciscoIfMonitorNotifMIB.setRevisions(('2002-10-11 00:00',))
_CIfMonNotifMIBNotifications_ObjectIdentity=ObjectIdentity
cIfMonNotifMIBNotifications=_CIfMonNotifMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,999,0))
_CIfMonNotifMIBObjects_ObjectIdentity=ObjectIdentity
cIfMonNotifMIBObjects=_CIfMonNotifMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,999,1))
class _CIfMonNotifCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CIfMonNotifCount_Type.__name__=_D
_CIfMonNotifCount_Object=MibScalar
cIfMonNotifCount=_CIfMonNotifCount_Object((1,3,6,1,4,1,9,10,999,1,1),_CIfMonNotifCount_Type())
cIfMonNotifCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cIfMonNotifCount.setStatus(_B)
_CIfMonNotifTable_Object=MibTable
cIfMonNotifTable=_CIfMonNotifTable_Object((1,3,6,1,4,1,9,10,999,1,2))
if mibBuilder.loadTexts:cIfMonNotifTable.setStatus(_B)
_CIfMonNotifEntry_Object=MibTableRow
cIfMonNotifEntry=_CIfMonNotifEntry_Object((1,3,6,1,4,1,9,10,999,1,2,1))
cIfMonNotifEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cIfMonNotifEntry.setStatus(_B)
_CIfMonNotifLastChange_Type=TimeStamp
_CIfMonNotifLastChange_Object=MibTableColumn
cIfMonNotifLastChange=_CIfMonNotifLastChange_Object((1,3,6,1,4,1,9,10,999,1,2,1,1),_CIfMonNotifLastChange_Type())
cIfMonNotifLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:cIfMonNotifLastChange.setStatus(_B)
class _CIfMonNotifSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('red',1),('yellow',2)))
_CIfMonNotifSeverity_Type.__name__=_G
_CIfMonNotifSeverity_Object=MibTableColumn
cIfMonNotifSeverity=_CIfMonNotifSeverity_Object((1,3,6,1,4,1,9,10,999,1,2,1,2),_CIfMonNotifSeverity_Type())
cIfMonNotifSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cIfMonNotifSeverity.setStatus(_B)
class _CIfMonNotifCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('aborts',1),('crc',2),('drops',3),('flaps',4),('frame-reject',5),('runts',6),('sabm',7),('frmr',8),('disc',9)))
_CIfMonNotifCause_Type.__name__=_G
_CIfMonNotifCause_Object=MibTableColumn
cIfMonNotifCause=_CIfMonNotifCause_Object((1,3,6,1,4,1,9,10,999,1,2,1,3),_CIfMonNotifCause_Type())
cIfMonNotifCause.setMaxAccess(_C)
if mibBuilder.loadTexts:cIfMonNotifCause.setStatus(_B)
class _CIfMonNotifValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CIfMonNotifValue_Type.__name__=_D
_CIfMonNotifValue_Object=MibTableColumn
cIfMonNotifValue=_CIfMonNotifValue_Object((1,3,6,1,4,1,9,10,999,1,2,1,4),_CIfMonNotifValue_Type())
cIfMonNotifValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cIfMonNotifValue.setStatus(_B)
class _CIfMonNotifThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000))
_CIfMonNotifThreshold_Type.__name__=_D
_CIfMonNotifThreshold_Object=MibTableColumn
cIfMonNotifThreshold=_CIfMonNotifThreshold_Object((1,3,6,1,4,1,9,10,999,1,2,1,5),_CIfMonNotifThreshold_Type())
cIfMonNotifThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cIfMonNotifThreshold.setStatus(_B)
class _CIfMonNotifInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,600))
_CIfMonNotifInterval_Type.__name__=_D
_CIfMonNotifInterval_Object=MibTableColumn
cIfMonNotifInterval=_CIfMonNotifInterval_Object((1,3,6,1,4,1,9,10,999,1,2,1,6),_CIfMonNotifInterval_Type())
cIfMonNotifInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cIfMonNotifInterval.setStatus(_B)
if mibBuilder.loadTexts:cIfMonNotifInterval.setUnits('seconds')
_CIfMonNotifMIBConformance_ObjectIdentity=ObjectIdentity
cIfMonNotifMIBConformance=_CIfMonNotifMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,999,2))
_CIfMonNotifMIBCompliances_ObjectIdentity=ObjectIdentity
cIfMonNotifMIBCompliances=_CIfMonNotifMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,999,2,1))
_CIfMonNotifMIBGroups_ObjectIdentity=ObjectIdentity
cIfMonNotifMIBGroups=_CIfMonNotifMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,999,2,2))
cIfMonNotifObjectGroup=ObjectGroup((1,3,6,1,4,1,9,10,999,2,2,1))
cIfMonNotifObjectGroup.setObjects(*((_A,_H),(_A,_N),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:cIfMonNotifObjectGroup.setStatus(_B)
cIfMonNotifEvent=NotificationType((1,3,6,1,4,1,9,10,999,0,1))
cIfMonNotifEvent.setObjects(*((_E,_F),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:cIfMonNotifEvent.setStatus(_B)
cIfMonNotifEventGroup=NotificationGroup((1,3,6,1,4,1,9,10,999,2,2,2))
cIfMonNotifEventGroup.setObjects((_A,_O))
if mibBuilder.loadTexts:cIfMonNotifEventGroup.setStatus(_B)
cIfMonNotifMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,999,2,1,1))
cIfMonNotifMIBCompliance.setObjects(*((_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:cIfMonNotifMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoIfMonitorNotifMIB':ciscoIfMonitorNotifMIB,'cIfMonNotifMIBNotifications':cIfMonNotifMIBNotifications,_O:cIfMonNotifEvent,'cIfMonNotifMIBObjects':cIfMonNotifMIBObjects,_H:cIfMonNotifCount,'cIfMonNotifTable':cIfMonNotifTable,'cIfMonNotifEntry':cIfMonNotifEntry,_N:cIfMonNotifLastChange,_I:cIfMonNotifSeverity,_J:cIfMonNotifCause,_K:cIfMonNotifValue,_L:cIfMonNotifThreshold,_M:cIfMonNotifInterval,'cIfMonNotifMIBConformance':cIfMonNotifMIBConformance,'cIfMonNotifMIBCompliances':cIfMonNotifMIBCompliances,'cIfMonNotifMIBCompliance':cIfMonNotifMIBCompliance,'cIfMonNotifMIBGroups':cIfMonNotifMIBGroups,_P:cIfMonNotifObjectGroup,_Q:cIfMonNotifEventGroup})