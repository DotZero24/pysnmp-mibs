_S='dpSyslogLogServerGroup'
_R='dpSyslogGeneralGroup'
_Q='dpSyslogServerFacility'
_P='dpSyslogServerSeverity'
_O='dpSyslogServerPort'
_N='dpSyslogLogOnEnabled'
_M='dpSyslogBufferDescription'
_L='dpSyslogBufferDateAndTime'
_K='dpSyslogBufferTableNum'
_J='dpSyslogLogBufferEnabled'
_I='dpSyslogClearLogBuffer'
_H='Unsigned32'
_G='ifIndex'
_F='IF-MIB'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='DLINKPRIME-SYSLOG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_F,'InterfaceIndexOrZero',_G)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
SyslogFacility,SyslogSeverity=mibBuilder.importSymbols('SYSLOG-TC-MIB','SyslogFacility','SyslogSeverity')
dlinkPrimeSyslogMIB=ModuleIdentity((1,3,6,1,4,1,171,15,21))
if mibBuilder.loadTexts:dlinkPrimeSyslogMIB.setRevisions(('2014-04-26 00:00',))
_DpSyslogMIBNotifications_ObjectIdentity=ObjectIdentity
dpSyslogMIBNotifications=_DpSyslogMIBNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,21,0))
_DpSyslogMIBObjects_ObjectIdentity=ObjectIdentity
dpSyslogMIBObjects=_DpSyslogMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,21,1))
_DpSyslogGeneral_ObjectIdentity=ObjectIdentity
dpSyslogGeneral=_DpSyslogGeneral_ObjectIdentity((1,3,6,1,4,1,171,15,21,1,1))
_DpSyslogLogOnEnabled_Type=TruthValue
_DpSyslogLogOnEnabled_Object=MibScalar
dpSyslogLogOnEnabled=_DpSyslogLogOnEnabled_Object((1,3,6,1,4,1,171,15,21,1,1,1),_DpSyslogLogOnEnabled_Type())
dpSyslogLogOnEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dpSyslogLogOnEnabled.setStatus(_A)
_DpSyslogLogbuffer_ObjectIdentity=ObjectIdentity
dpSyslogLogbuffer=_DpSyslogLogbuffer_ObjectIdentity((1,3,6,1,4,1,171,15,21,1,2))
if mibBuilder.loadTexts:dpSyslogLogbuffer.setStatus(_A)
class _DpSyslogClearLogBuffer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),('noOp',2)))
_DpSyslogClearLogBuffer_Type.__name__=_D
_DpSyslogClearLogBuffer_Object=MibScalar
dpSyslogClearLogBuffer=_DpSyslogClearLogBuffer_Object((1,3,6,1,4,1,171,15,21,1,2,1),_DpSyslogClearLogBuffer_Type())
dpSyslogClearLogBuffer.setMaxAccess(_C)
if mibBuilder.loadTexts:dpSyslogClearLogBuffer.setStatus(_A)
_DpSyslogLogBufferEnabled_Type=TruthValue
_DpSyslogLogBufferEnabled_Object=MibScalar
dpSyslogLogBufferEnabled=_DpSyslogLogBufferEnabled_Object((1,3,6,1,4,1,171,15,21,1,2,2),_DpSyslogLogBufferEnabled_Type())
dpSyslogLogBufferEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dpSyslogLogBufferEnabled.setStatus(_A)
_DpSyslogServer_ObjectIdentity=ObjectIdentity
dpSyslogServer=_DpSyslogServer_ObjectIdentity((1,3,6,1,4,1,171,15,21,1,3))
_DpSyslogServerAddress_Type=IpAddress
_DpSyslogServerAddress_Object=MibScalar
dpSyslogServerAddress=_DpSyslogServerAddress_Object((1,3,6,1,4,1,171,15,21,1,3,1),_DpSyslogServerAddress_Type())
dpSyslogServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dpSyslogServerAddress.setStatus(_A)
class _DpSyslogServerPort_Type(Unsigned32):defaultValue=514;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(514,514),ValueRangeConstraint(1024,65535))
_DpSyslogServerPort_Type.__name__=_H
_DpSyslogServerPort_Object=MibScalar
dpSyslogServerPort=_DpSyslogServerPort_Object((1,3,6,1,4,1,171,15,21,1,3,2),_DpSyslogServerPort_Type())
dpSyslogServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dpSyslogServerPort.setStatus(_A)
class _DpSyslogServerSeverity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('warning',1),('informational',2),('all',3)))
_DpSyslogServerSeverity_Type.__name__=_D
_DpSyslogServerSeverity_Object=MibScalar
dpSyslogServerSeverity=_DpSyslogServerSeverity_Object((1,3,6,1,4,1,171,15,21,1,3,3),_DpSyslogServerSeverity_Type())
dpSyslogServerSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:dpSyslogServerSeverity.setStatus(_A)
class _DpSyslogServerFacility_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('local_0',0),('local_1',1),('local_2',2),('local_3',3),('local_4',4),('local_5',5),('local_6',6),('local_7',7)))
_DpSyslogServerFacility_Type.__name__=_D
_DpSyslogServerFacility_Object=MibScalar
dpSyslogServerFacility=_DpSyslogServerFacility_Object((1,3,6,1,4,1,171,15,21,1,3,4),_DpSyslogServerFacility_Type())
dpSyslogServerFacility.setMaxAccess(_C)
if mibBuilder.loadTexts:dpSyslogServerFacility.setStatus(_A)
_DpSyslogBufferTableNum_Type=Unsigned32
_DpSyslogBufferTableNum_Object=MibScalar
dpSyslogBufferTableNum=_DpSyslogBufferTableNum_Object((1,3,6,1,4,1,171,15,21,1,4),_DpSyslogBufferTableNum_Type())
dpSyslogBufferTableNum.setMaxAccess(_E)
if mibBuilder.loadTexts:dpSyslogBufferTableNum.setStatus(_A)
_DpSyslogBufferTable_Object=MibTable
dpSyslogBufferTable=_DpSyslogBufferTable_Object((1,3,6,1,4,1,171,15,21,1,5))
if mibBuilder.loadTexts:dpSyslogBufferTable.setStatus(_A)
_DpSyslogBufferEntry_Object=MibTableRow
dpSyslogBufferEntry=_DpSyslogBufferEntry_Object((1,3,6,1,4,1,171,15,21,1,5,1))
dpSyslogBufferEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dpSyslogBufferEntry.setStatus(_A)
_DpSyslogBufferLevel_Type=DisplayString
_DpSyslogBufferLevel_Object=MibTableColumn
dpSyslogBufferLevel=_DpSyslogBufferLevel_Object((1,3,6,1,4,1,171,15,21,1,5,1,1),_DpSyslogBufferLevel_Type())
dpSyslogBufferLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:dpSyslogBufferLevel.setStatus(_A)
_DpSyslogBufferDateAndTime_Type=DisplayString
_DpSyslogBufferDateAndTime_Object=MibTableColumn
dpSyslogBufferDateAndTime=_DpSyslogBufferDateAndTime_Object((1,3,6,1,4,1,171,15,21,1,5,1,2),_DpSyslogBufferDateAndTime_Type())
dpSyslogBufferDateAndTime.setMaxAccess(_E)
if mibBuilder.loadTexts:dpSyslogBufferDateAndTime.setStatus(_A)
_DpSyslogBufferDescription_Type=DisplayString
_DpSyslogBufferDescription_Object=MibTableColumn
dpSyslogBufferDescription=_DpSyslogBufferDescription_Object((1,3,6,1,4,1,171,15,21,1,5,1,3),_DpSyslogBufferDescription_Type())
dpSyslogBufferDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:dpSyslogBufferDescription.setStatus(_A)
_DpSyslogMIBConformance_ObjectIdentity=ObjectIdentity
dpSyslogMIBConformance=_DpSyslogMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,21,2))
_DpSyslogMIBCompliances_ObjectIdentity=ObjectIdentity
dpSyslogMIBCompliances=_DpSyslogMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,21,2,1))
_DpSyslogMIBGroups_ObjectIdentity=ObjectIdentity
dpSyslogMIBGroups=_DpSyslogMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,15,21,2,1,2))
dpSyslogGeneralGroup=ObjectGroup((1,3,6,1,4,1,171,15,21,2,1,2,1))
dpSyslogGeneralGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:dpSyslogGeneralGroup.setStatus(_A)
dpSyslogLogServerGroup=ObjectGroup((1,3,6,1,4,1,171,15,21,2,1,2,2))
dpSyslogLogServerGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:dpSyslogLogServerGroup.setStatus(_A)
dpSyslogMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,21,2,1,1))
dpSyslogMIBCompliance.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:dpSyslogMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlinkPrimeSyslogMIB':dlinkPrimeSyslogMIB,'dpSyslogMIBNotifications':dpSyslogMIBNotifications,'dpSyslogMIBObjects':dpSyslogMIBObjects,'dpSyslogGeneral':dpSyslogGeneral,_N:dpSyslogLogOnEnabled,'dpSyslogLogbuffer':dpSyslogLogbuffer,_I:dpSyslogClearLogBuffer,_J:dpSyslogLogBufferEnabled,'dpSyslogServer':dpSyslogServer,'dpSyslogServerAddress':dpSyslogServerAddress,_O:dpSyslogServerPort,_P:dpSyslogServerSeverity,_Q:dpSyslogServerFacility,_K:dpSyslogBufferTableNum,'dpSyslogBufferTable':dpSyslogBufferTable,'dpSyslogBufferEntry':dpSyslogBufferEntry,'dpSyslogBufferLevel':dpSyslogBufferLevel,_L:dpSyslogBufferDateAndTime,_M:dpSyslogBufferDescription,'dpSyslogMIBConformance':dpSyslogMIBConformance,'dpSyslogMIBCompliances':dpSyslogMIBCompliances,'dpSyslogMIBCompliance':dpSyslogMIBCompliance,'dpSyslogMIBGroups':dpSyslogMIBGroups,_R:dpSyslogGeneralGroup,_S:dpSyslogLogServerGroup})