_M='oraListenerState'
_L='oraListenAddressIndex'
_K='oraPrespawnedSrvIndex'
_J='blocked'
_I='oraDispatcherIndex'
_H='oraDedicatedSrvIndex'
_G='NotificationType'
_F='oraListenerIndex'
_E='oraSIDName'
_D='Integer32'
_C='ORALISTENER-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_G,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_G,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Oracle_ObjectIdentity=ObjectIdentity
oracle=_Oracle_ObjectIdentity((1,3,6,1,4,1,111))
_OraListenerMIB_ObjectIdentity=ObjectIdentity
oraListenerMIB=_OraListenerMIB_ObjectIdentity((1,3,6,1,4,1,111,5))
_OraListenerObjects_ObjectIdentity=ObjectIdentity
oraListenerObjects=_OraListenerObjects_ObjectIdentity((1,3,6,1,4,1,111,5,1))
_OraListenerTable_Object=MibTable
oraListenerTable=_OraListenerTable_Object((1,3,6,1,4,1,111,5,1,1))
if mibBuilder.loadTexts:oraListenerTable.setStatus(_A)
_OraListenerEntry_Object=MibTableRow
oraListenerEntry=_OraListenerEntry_Object((1,3,6,1,4,1,111,5,1,1,1))
oraListenerEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:oraListenerEntry.setStatus(_A)
_OraListenerIndex_Type=Integer32
_OraListenerIndex_Object=MibTableColumn
oraListenerIndex=_OraListenerIndex_Object((1,3,6,1,4,1,111,5,1,1,1,1),_OraListenerIndex_Type())
oraListenerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oraListenerIndex.setStatus(_A)
_OraListenerName_Type=DisplayString
_OraListenerName_Object=MibTableColumn
oraListenerName=_OraListenerName_Object((1,3,6,1,4,1,111,5,1,1,1,2),_OraListenerName_Type())
oraListenerName.setMaxAccess(_B)
if mibBuilder.loadTexts:oraListenerName.setStatus(_A)
_OraListenerVersion_Type=DisplayString
_OraListenerVersion_Object=MibTableColumn
oraListenerVersion=_OraListenerVersion_Object((1,3,6,1,4,1,111,5,1,1,1,3),_OraListenerVersion_Type())
oraListenerVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:oraListenerVersion.setStatus(_A)
_OraListenerStartDate_Type=DisplayString
_OraListenerStartDate_Object=MibTableColumn
oraListenerStartDate=_OraListenerStartDate_Object((1,3,6,1,4,1,111,5,1,1,1,4),_OraListenerStartDate_Type())
oraListenerStartDate.setMaxAccess(_B)
if mibBuilder.loadTexts:oraListenerStartDate.setStatus(_A)
_OraListenerUptime_Type=TimeTicks
_OraListenerUptime_Object=MibTableColumn
oraListenerUptime=_OraListenerUptime_Object((1,3,6,1,4,1,111,5,1,1,1,5),_OraListenerUptime_Type())
oraListenerUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:oraListenerUptime.setStatus(_A)
class _OraListenerTraceLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('level1',1),('level2',2),('level3',3),('user',4),('level5',5),('admin',6),('level7',7),('level8',8),('level9',9),('level10',10),('level11',11),('level12',12),('level13',13),('level14',14),('level15',15),('level16',16),('off',17)))
_OraListenerTraceLevel_Type.__name__=_D
_OraListenerTraceLevel_Object=MibTableColumn
oraListenerTraceLevel=_OraListenerTraceLevel_Object((1,3,6,1,4,1,111,5,1,1,1,6),_OraListenerTraceLevel_Type())
oraListenerTraceLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:oraListenerTraceLevel.setStatus(_A)
class _OraListenerSecurityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_OraListenerSecurityLevel_Type.__name__=_D
_OraListenerSecurityLevel_Object=MibTableColumn
oraListenerSecurityLevel=_OraListenerSecurityLevel_Object((1,3,6,1,4,1,111,5,1,1,1,7),_OraListenerSecurityLevel_Type())
oraListenerSecurityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:oraListenerSecurityLevel.setStatus(_A)
_OraListenerParameterFile_Type=DisplayString
_OraListenerParameterFile_Object=MibTableColumn
oraListenerParameterFile=_OraListenerParameterFile_Object((1,3,6,1,4,1,111,5,1,1,1,8),_OraListenerParameterFile_Type())
oraListenerParameterFile.setMaxAccess(_B)
if mibBuilder.loadTexts:oraListenerParameterFile.setStatus(_A)
_OraListenerLogFile_Type=DisplayString
_OraListenerLogFile_Object=MibTableColumn
oraListenerLogFile=_OraListenerLogFile_Object((1,3,6,1,4,1,111,5,1,1,1,9),_OraListenerLogFile_Type())
oraListenerLogFile.setMaxAccess(_B)
if mibBuilder.loadTexts:oraListenerLogFile.setStatus(_A)
_OraListenerTraceFile_Type=DisplayString
_OraListenerTraceFile_Object=MibTableColumn
oraListenerTraceFile=_OraListenerTraceFile_Object((1,3,6,1,4,1,111,5,1,1,1,10),_OraListenerTraceFile_Type())
oraListenerTraceFile.setMaxAccess(_B)
if mibBuilder.loadTexts:oraListenerTraceFile.setStatus(_A)
class _OraListenerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_OraListenerState_Type.__name__=_D
_OraListenerState_Object=MibTableColumn
oraListenerState=_OraListenerState_Object((1,3,6,1,4,1,111,5,1,1,1,11),_OraListenerState_Type())
oraListenerState.setMaxAccess(_B)
if mibBuilder.loadTexts:oraListenerState.setStatus(_A)
_OraListenerNumberOfServices_Type=Integer32
_OraListenerNumberOfServices_Object=MibTableColumn
oraListenerNumberOfServices=_OraListenerNumberOfServices_Object((1,3,6,1,4,1,111,5,1,1,1,12),_OraListenerNumberOfServices_Type())
oraListenerNumberOfServices.setMaxAccess(_B)
if mibBuilder.loadTexts:oraListenerNumberOfServices.setStatus(_A)
_OraListenerContact_Type=DisplayString
_OraListenerContact_Object=MibTableColumn
oraListenerContact=_OraListenerContact_Object((1,3,6,1,4,1,111,5,1,1,1,13),_OraListenerContact_Type())
oraListenerContact.setMaxAccess('read-write')
if mibBuilder.loadTexts:oraListenerContact.setStatus(_A)
_OraDedicatedSrvTable_Object=MibTable
oraDedicatedSrvTable=_OraDedicatedSrvTable_Object((1,3,6,1,4,1,111,5,1,2))
if mibBuilder.loadTexts:oraDedicatedSrvTable.setStatus(_A)
_OraDedicatedSrvEntry_Object=MibTableRow
oraDedicatedSrvEntry=_OraDedicatedSrvEntry_Object((1,3,6,1,4,1,111,5,1,2,1))
oraDedicatedSrvEntry.setIndexNames((0,_C,_E),(0,_C,_H))
if mibBuilder.loadTexts:oraDedicatedSrvEntry.setStatus(_A)
_OraDedicatedSrvIndex_Type=Integer32
_OraDedicatedSrvIndex_Object=MibTableColumn
oraDedicatedSrvIndex=_OraDedicatedSrvIndex_Object((1,3,6,1,4,1,111,5,1,2,1,1),_OraDedicatedSrvIndex_Type())
oraDedicatedSrvIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDedicatedSrvIndex.setStatus(_A)
_OraDedicatedSrvEstablishedConnections_Type=Counter32
_OraDedicatedSrvEstablishedConnections_Object=MibTableColumn
oraDedicatedSrvEstablishedConnections=_OraDedicatedSrvEstablishedConnections_Object((1,3,6,1,4,1,111,5,1,2,1,2),_OraDedicatedSrvEstablishedConnections_Type())
oraDedicatedSrvEstablishedConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDedicatedSrvEstablishedConnections.setStatus(_A)
_OraDedicatedSrvRejectedConnections_Type=Counter32
_OraDedicatedSrvRejectedConnections_Object=MibTableColumn
oraDedicatedSrvRejectedConnections=_OraDedicatedSrvRejectedConnections_Object((1,3,6,1,4,1,111,5,1,2,1,3),_OraDedicatedSrvRejectedConnections_Type())
oraDedicatedSrvRejectedConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDedicatedSrvRejectedConnections.setStatus(_A)
_OraDispatcherTable_Object=MibTable
oraDispatcherTable=_OraDispatcherTable_Object((1,3,6,1,4,1,111,5,1,3))
if mibBuilder.loadTexts:oraDispatcherTable.setStatus(_A)
_OraDispatcherEntry_Object=MibTableRow
oraDispatcherEntry=_OraDispatcherEntry_Object((1,3,6,1,4,1,111,5,1,3,1))
oraDispatcherEntry.setIndexNames((0,_C,_E),(0,_C,_I))
if mibBuilder.loadTexts:oraDispatcherEntry.setStatus(_A)
_OraDispatcherIndex_Type=Integer32
_OraDispatcherIndex_Object=MibTableColumn
oraDispatcherIndex=_OraDispatcherIndex_Object((1,3,6,1,4,1,111,5,1,3,1,1),_OraDispatcherIndex_Type())
oraDispatcherIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDispatcherIndex.setStatus(_A)
_OraDispatcherEstablishedConnections_Type=Counter32
_OraDispatcherEstablishedConnections_Object=MibTableColumn
oraDispatcherEstablishedConnections=_OraDispatcherEstablishedConnections_Object((1,3,6,1,4,1,111,5,1,3,1,2),_OraDispatcherEstablishedConnections_Type())
oraDispatcherEstablishedConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDispatcherEstablishedConnections.setStatus(_A)
_OraDispatcherRejectedConnections_Type=Counter32
_OraDispatcherRejectedConnections_Object=MibTableColumn
oraDispatcherRejectedConnections=_OraDispatcherRejectedConnections_Object((1,3,6,1,4,1,111,5,1,3,1,3),_OraDispatcherRejectedConnections_Type())
oraDispatcherRejectedConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDispatcherRejectedConnections.setStatus(_A)
_OraDispatcherCurrentConnections_Type=Gauge32
_OraDispatcherCurrentConnections_Object=MibTableColumn
oraDispatcherCurrentConnections=_OraDispatcherCurrentConnections_Object((1,3,6,1,4,1,111,5,1,3,1,4),_OraDispatcherCurrentConnections_Type())
oraDispatcherCurrentConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDispatcherCurrentConnections.setStatus(_A)
_OraDispatcherMaximumConnections_Type=Integer32
_OraDispatcherMaximumConnections_Object=MibTableColumn
oraDispatcherMaximumConnections=_OraDispatcherMaximumConnections_Object((1,3,6,1,4,1,111,5,1,3,1,5),_OraDispatcherMaximumConnections_Type())
oraDispatcherMaximumConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDispatcherMaximumConnections.setStatus(_A)
class _OraDispatcherState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('ready',2)))
_OraDispatcherState_Type.__name__=_D
_OraDispatcherState_Object=MibTableColumn
oraDispatcherState=_OraDispatcherState_Object((1,3,6,1,4,1,111,5,1,3,1,6),_OraDispatcherState_Type())
oraDispatcherState.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDispatcherState.setStatus(_A)
_OraDispatcherProtocolInfo_Type=DisplayString
_OraDispatcherProtocolInfo_Object=MibTableColumn
oraDispatcherProtocolInfo=_OraDispatcherProtocolInfo_Object((1,3,6,1,4,1,111,5,1,3,1,7),_OraDispatcherProtocolInfo_Type())
oraDispatcherProtocolInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDispatcherProtocolInfo.setStatus(_A)
_OraPrespawnedSrvTable_Object=MibTable
oraPrespawnedSrvTable=_OraPrespawnedSrvTable_Object((1,3,6,1,4,1,111,5,1,4))
if mibBuilder.loadTexts:oraPrespawnedSrvTable.setStatus(_A)
_OraPrespawnedSrvEntry_Object=MibTableRow
oraPrespawnedSrvEntry=_OraPrespawnedSrvEntry_Object((1,3,6,1,4,1,111,5,1,4,1))
oraPrespawnedSrvEntry.setIndexNames((0,_C,_E),(0,_C,_K))
if mibBuilder.loadTexts:oraPrespawnedSrvEntry.setStatus(_A)
_OraPrespawnedSrvIndex_Type=Integer32
_OraPrespawnedSrvIndex_Object=MibTableColumn
oraPrespawnedSrvIndex=_OraPrespawnedSrvIndex_Object((1,3,6,1,4,1,111,5,1,4,1,1),_OraPrespawnedSrvIndex_Type())
oraPrespawnedSrvIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oraPrespawnedSrvIndex.setStatus(_A)
_OraPrespawnedSrvEstablishedConnections_Type=Counter32
_OraPrespawnedSrvEstablishedConnections_Object=MibTableColumn
oraPrespawnedSrvEstablishedConnections=_OraPrespawnedSrvEstablishedConnections_Object((1,3,6,1,4,1,111,5,1,4,1,2),_OraPrespawnedSrvEstablishedConnections_Type())
oraPrespawnedSrvEstablishedConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:oraPrespawnedSrvEstablishedConnections.setStatus(_A)
_OraPrespawnedSrvRejectedConnections_Type=Counter32
_OraPrespawnedSrvRejectedConnections_Object=MibTableColumn
oraPrespawnedSrvRejectedConnections=_OraPrespawnedSrvRejectedConnections_Object((1,3,6,1,4,1,111,5,1,4,1,3),_OraPrespawnedSrvRejectedConnections_Type())
oraPrespawnedSrvRejectedConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:oraPrespawnedSrvRejectedConnections.setStatus(_A)
_OraPrespawnedSrvCurrentConnections_Type=Gauge32
_OraPrespawnedSrvCurrentConnections_Object=MibTableColumn
oraPrespawnedSrvCurrentConnections=_OraPrespawnedSrvCurrentConnections_Object((1,3,6,1,4,1,111,5,1,4,1,4),_OraPrespawnedSrvCurrentConnections_Type())
oraPrespawnedSrvCurrentConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:oraPrespawnedSrvCurrentConnections.setStatus(_A)
_OraPrespawnedSrvMaximumConnections_Type=Integer32
_OraPrespawnedSrvMaximumConnections_Object=MibTableColumn
oraPrespawnedSrvMaximumConnections=_OraPrespawnedSrvMaximumConnections_Object((1,3,6,1,4,1,111,5,1,4,1,5),_OraPrespawnedSrvMaximumConnections_Type())
oraPrespawnedSrvMaximumConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:oraPrespawnedSrvMaximumConnections.setStatus(_A)
class _OraPrespawnedSrvState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('ready',2)))
_OraPrespawnedSrvState_Type.__name__=_D
_OraPrespawnedSrvState_Object=MibTableColumn
oraPrespawnedSrvState=_OraPrespawnedSrvState_Object((1,3,6,1,4,1,111,5,1,4,1,6),_OraPrespawnedSrvState_Type())
oraPrespawnedSrvState.setMaxAccess(_B)
if mibBuilder.loadTexts:oraPrespawnedSrvState.setStatus(_A)
_OraPrespawnedSrvProtocolInfo_Type=DisplayString
_OraPrespawnedSrvProtocolInfo_Object=MibTableColumn
oraPrespawnedSrvProtocolInfo=_OraPrespawnedSrvProtocolInfo_Object((1,3,6,1,4,1,111,5,1,4,1,7),_OraPrespawnedSrvProtocolInfo_Type())
oraPrespawnedSrvProtocolInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:oraPrespawnedSrvProtocolInfo.setStatus(_A)
_OraPrespawnedSrvProcessorID_Type=DisplayString
_OraPrespawnedSrvProcessorID_Object=MibTableColumn
oraPrespawnedSrvProcessorID=_OraPrespawnedSrvProcessorID_Object((1,3,6,1,4,1,111,5,1,4,1,8),_OraPrespawnedSrvProcessorID_Type())
oraPrespawnedSrvProcessorID.setMaxAccess(_B)
if mibBuilder.loadTexts:oraPrespawnedSrvProcessorID.setStatus(_A)
_OraSIDTable_Object=MibTable
oraSIDTable=_OraSIDTable_Object((1,3,6,1,4,1,111,5,1,5))
if mibBuilder.loadTexts:oraSIDTable.setStatus(_A)
_OraSIDEntry_Object=MibTableRow
oraSIDEntry=_OraSIDEntry_Object((1,3,6,1,4,1,111,5,1,5,1))
oraSIDEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:oraSIDEntry.setStatus(_A)
_OraSIDListenerIndex_Type=Integer32
_OraSIDListenerIndex_Object=MibTableColumn
oraSIDListenerIndex=_OraSIDListenerIndex_Object((1,3,6,1,4,1,111,5,1,5,1,1),_OraSIDListenerIndex_Type())
oraSIDListenerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oraSIDListenerIndex.setStatus(_A)
_OraSIDName_Type=DisplayString
_OraSIDName_Object=MibTableColumn
oraSIDName=_OraSIDName_Object((1,3,6,1,4,1,111,5,1,5,1,2),_OraSIDName_Type())
oraSIDName.setMaxAccess(_B)
if mibBuilder.loadTexts:oraSIDName.setStatus(_A)
_OraSIDCurrentConnectedClients_Type=Gauge32
_OraSIDCurrentConnectedClients_Object=MibTableColumn
oraSIDCurrentConnectedClients=_OraSIDCurrentConnectedClients_Object((1,3,6,1,4,1,111,5,1,5,1,3),_OraSIDCurrentConnectedClients_Type())
oraSIDCurrentConnectedClients.setMaxAccess(_B)
if mibBuilder.loadTexts:oraSIDCurrentConnectedClients.setStatus(_A)
_OraSIDReservedConnections_Type=Counter32
_OraSIDReservedConnections_Object=MibTableColumn
oraSIDReservedConnections=_OraSIDReservedConnections_Object((1,3,6,1,4,1,111,5,1,5,1,4),_OraSIDReservedConnections_Type())
oraSIDReservedConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:oraSIDReservedConnections.setStatus(_A)
_OraListenAddressTable_Object=MibTable
oraListenAddressTable=_OraListenAddressTable_Object((1,3,6,1,4,1,111,5,1,6))
if mibBuilder.loadTexts:oraListenAddressTable.setStatus(_A)
_OraListenAddressEntry_Object=MibTableRow
oraListenAddressEntry=_OraListenAddressEntry_Object((1,3,6,1,4,1,111,5,1,6,1))
oraListenAddressEntry.setIndexNames((0,_C,_F),(0,_C,_L))
if mibBuilder.loadTexts:oraListenAddressEntry.setStatus(_A)
_OraListenAddressIndex_Type=Integer32
_OraListenAddressIndex_Object=MibTableColumn
oraListenAddressIndex=_OraListenAddressIndex_Object((1,3,6,1,4,1,111,5,1,6,1,1),_OraListenAddressIndex_Type())
oraListenAddressIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oraListenAddressIndex.setStatus(_A)
_OraListenAddress_Type=DisplayString
_OraListenAddress_Object=MibTableColumn
oraListenAddress=_OraListenAddress_Object((1,3,6,1,4,1,111,5,1,6,1,2),_OraListenAddress_Type())
oraListenAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oraListenAddress.setStatus(_A)
_OraListenerTraps_ObjectIdentity=ObjectIdentity
oraListenerTraps=_OraListenerTraps_ObjectIdentity((1,3,6,1,4,1,111,5,2))
oraListenerStateChange=NotificationType((1,3,6,1,4,1,111,5,2,0,1))
oraListenerStateChange.setObjects((_C,_M))
if mibBuilder.loadTexts:oraListenerStateChange.setStatus('')
mibBuilder.exportSymbols(_C,**{'oracle':oracle,'oraListenerMIB':oraListenerMIB,'oraListenerObjects':oraListenerObjects,'oraListenerTable':oraListenerTable,'oraListenerEntry':oraListenerEntry,_F:oraListenerIndex,'oraListenerName':oraListenerName,'oraListenerVersion':oraListenerVersion,'oraListenerStartDate':oraListenerStartDate,'oraListenerUptime':oraListenerUptime,'oraListenerTraceLevel':oraListenerTraceLevel,'oraListenerSecurityLevel':oraListenerSecurityLevel,'oraListenerParameterFile':oraListenerParameterFile,'oraListenerLogFile':oraListenerLogFile,'oraListenerTraceFile':oraListenerTraceFile,_M:oraListenerState,'oraListenerNumberOfServices':oraListenerNumberOfServices,'oraListenerContact':oraListenerContact,'oraDedicatedSrvTable':oraDedicatedSrvTable,'oraDedicatedSrvEntry':oraDedicatedSrvEntry,_H:oraDedicatedSrvIndex,'oraDedicatedSrvEstablishedConnections':oraDedicatedSrvEstablishedConnections,'oraDedicatedSrvRejectedConnections':oraDedicatedSrvRejectedConnections,'oraDispatcherTable':oraDispatcherTable,'oraDispatcherEntry':oraDispatcherEntry,_I:oraDispatcherIndex,'oraDispatcherEstablishedConnections':oraDispatcherEstablishedConnections,'oraDispatcherRejectedConnections':oraDispatcherRejectedConnections,'oraDispatcherCurrentConnections':oraDispatcherCurrentConnections,'oraDispatcherMaximumConnections':oraDispatcherMaximumConnections,'oraDispatcherState':oraDispatcherState,'oraDispatcherProtocolInfo':oraDispatcherProtocolInfo,'oraPrespawnedSrvTable':oraPrespawnedSrvTable,'oraPrespawnedSrvEntry':oraPrespawnedSrvEntry,_K:oraPrespawnedSrvIndex,'oraPrespawnedSrvEstablishedConnections':oraPrespawnedSrvEstablishedConnections,'oraPrespawnedSrvRejectedConnections':oraPrespawnedSrvRejectedConnections,'oraPrespawnedSrvCurrentConnections':oraPrespawnedSrvCurrentConnections,'oraPrespawnedSrvMaximumConnections':oraPrespawnedSrvMaximumConnections,'oraPrespawnedSrvState':oraPrespawnedSrvState,'oraPrespawnedSrvProtocolInfo':oraPrespawnedSrvProtocolInfo,'oraPrespawnedSrvProcessorID':oraPrespawnedSrvProcessorID,'oraSIDTable':oraSIDTable,'oraSIDEntry':oraSIDEntry,'oraSIDListenerIndex':oraSIDListenerIndex,_E:oraSIDName,'oraSIDCurrentConnectedClients':oraSIDCurrentConnectedClients,'oraSIDReservedConnections':oraSIDReservedConnections,'oraListenAddressTable':oraListenAddressTable,'oraListenAddressEntry':oraListenAddressEntry,_L:oraListenAddressIndex,'oraListenAddress':oraListenAddress,'oraListenerTraps':oraListenerTraps,'oraListenerStateChange':oraListenerStateChange})