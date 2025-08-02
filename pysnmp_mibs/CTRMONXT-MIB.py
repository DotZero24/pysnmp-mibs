_L='ctDiscoveryNMMACAddress'
_K='ctDiscoveryNMNetworkAddress'
_J='ctDiscoveryNMIndex'
_I='ctDiscoveryMNNetworkAddress'
_H='ctDiscoveryMNMACAddress'
_G='ctDiscoveryMNIndex'
_F='ctDiscoveryControlIndex'
_E='Integer32'
_D='read-write'
_C='CTRMONXT-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctronRmon,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctronRmon')
EntryStatus,OwnerString=mibBuilder.importSymbols('RMON-MIB','EntryStatus','OwnerString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtDiscovery_ObjectIdentity=ObjectIdentity
ctDiscovery=_CtDiscovery_ObjectIdentity((1,3,6,1,4,1,52,4,3,2,20))
_CtDiscoveryProtocol_ObjectIdentity=ObjectIdentity
ctDiscoveryProtocol=_CtDiscoveryProtocol_ObjectIdentity((1,3,6,1,4,1,52,4,3,2,20,1))
_CtProtIP_ObjectIdentity=ObjectIdentity
ctProtIP=_CtProtIP_ObjectIdentity((1,3,6,1,4,1,52,4,3,2,20,1,1))
_CtProtNetware_ObjectIdentity=ObjectIdentity
ctProtNetware=_CtProtNetware_ObjectIdentity((1,3,6,1,4,1,52,4,3,2,20,1,2))
_CtProtDecNet_ObjectIdentity=ObjectIdentity
ctProtDecNet=_CtProtDecNet_ObjectIdentity((1,3,6,1,4,1,52,4,3,2,20,1,3))
_CtDiscoveryControlTable_Object=MibTable
ctDiscoveryControlTable=_CtDiscoveryControlTable_Object((1,3,6,1,4,1,52,4,3,2,20,2))
if mibBuilder.loadTexts:ctDiscoveryControlTable.setStatus(_A)
_CtDiscoveryControlEntry_Object=MibTableRow
ctDiscoveryControlEntry=_CtDiscoveryControlEntry_Object((1,3,6,1,4,1,52,4,3,2,20,2,1))
ctDiscoveryControlEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:ctDiscoveryControlEntry.setStatus(_A)
class _CtDiscoveryControlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtDiscoveryControlIndex_Type.__name__=_E
_CtDiscoveryControlIndex_Object=MibTableColumn
ctDiscoveryControlIndex=_CtDiscoveryControlIndex_Object((1,3,6,1,4,1,52,4,3,2,20,2,1,1),_CtDiscoveryControlIndex_Type())
ctDiscoveryControlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDiscoveryControlIndex.setStatus(_A)
_CtDiscoveryControlDataSource_Type=ObjectIdentifier
_CtDiscoveryControlDataSource_Object=MibTableColumn
ctDiscoveryControlDataSource=_CtDiscoveryControlDataSource_Object((1,3,6,1,4,1,52,4,3,2,20,2,1,2),_CtDiscoveryControlDataSource_Type())
ctDiscoveryControlDataSource.setMaxAccess(_D)
if mibBuilder.loadTexts:ctDiscoveryControlDataSource.setStatus(_A)
_CtDiscoveryControlProtocol_Type=ObjectIdentifier
_CtDiscoveryControlProtocol_Object=MibTableColumn
ctDiscoveryControlProtocol=_CtDiscoveryControlProtocol_Object((1,3,6,1,4,1,52,4,3,2,20,2,1,3),_CtDiscoveryControlProtocol_Type())
ctDiscoveryControlProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:ctDiscoveryControlProtocol.setStatus(_A)
_CtDiscoveryControlTableSize_Type=Integer32
_CtDiscoveryControlTableSize_Object=MibTableColumn
ctDiscoveryControlTableSize=_CtDiscoveryControlTableSize_Object((1,3,6,1,4,1,52,4,3,2,20,2,1,4),_CtDiscoveryControlTableSize_Type())
ctDiscoveryControlTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDiscoveryControlTableSize.setStatus(_A)
_CtDiscoveryControlLastDeleteTime_Type=TimeTicks
_CtDiscoveryControlLastDeleteTime_Object=MibTableColumn
ctDiscoveryControlLastDeleteTime=_CtDiscoveryControlLastDeleteTime_Object((1,3,6,1,4,1,52,4,3,2,20,2,1,5),_CtDiscoveryControlLastDeleteTime_Type())
ctDiscoveryControlLastDeleteTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDiscoveryControlLastDeleteTime.setStatus(_A)
_CtDiscoveryControlAgeInterval_Type=Integer32
_CtDiscoveryControlAgeInterval_Object=MibTableColumn
ctDiscoveryControlAgeInterval=_CtDiscoveryControlAgeInterval_Object((1,3,6,1,4,1,52,4,3,2,20,2,1,6),_CtDiscoveryControlAgeInterval_Type())
ctDiscoveryControlAgeInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ctDiscoveryControlAgeInterval.setStatus(_A)
_CtDiscoveryControlOwner_Type=OwnerString
_CtDiscoveryControlOwner_Object=MibTableColumn
ctDiscoveryControlOwner=_CtDiscoveryControlOwner_Object((1,3,6,1,4,1,52,4,3,2,20,2,1,7),_CtDiscoveryControlOwner_Type())
ctDiscoveryControlOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:ctDiscoveryControlOwner.setStatus(_A)
_CtDiscoveryControlStatus_Type=EntryStatus
_CtDiscoveryControlStatus_Object=MibTableColumn
ctDiscoveryControlStatus=_CtDiscoveryControlStatus_Object((1,3,6,1,4,1,52,4,3,2,20,2,1,8),_CtDiscoveryControlStatus_Type())
ctDiscoveryControlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctDiscoveryControlStatus.setStatus(_A)
_CtDiscoveryMNTable_Object=MibTable
ctDiscoveryMNTable=_CtDiscoveryMNTable_Object((1,3,6,1,4,1,52,4,3,2,20,3))
if mibBuilder.loadTexts:ctDiscoveryMNTable.setStatus(_A)
_CtDiscoveryMNEntry_Object=MibTableRow
ctDiscoveryMNEntry=_CtDiscoveryMNEntry_Object((1,3,6,1,4,1,52,4,3,2,20,3,1))
ctDiscoveryMNEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:ctDiscoveryMNEntry.setStatus(_A)
_CtDiscoveryMNMACAddress_Type=OctetString
_CtDiscoveryMNMACAddress_Object=MibTableColumn
ctDiscoveryMNMACAddress=_CtDiscoveryMNMACAddress_Object((1,3,6,1,4,1,52,4,3,2,20,3,1,1),_CtDiscoveryMNMACAddress_Type())
ctDiscoveryMNMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDiscoveryMNMACAddress.setStatus(_A)
_CtDiscoveryMNNetworkAddress_Type=OctetString
_CtDiscoveryMNNetworkAddress_Object=MibTableColumn
ctDiscoveryMNNetworkAddress=_CtDiscoveryMNNetworkAddress_Object((1,3,6,1,4,1,52,4,3,2,20,3,1,2),_CtDiscoveryMNNetworkAddress_Type())
ctDiscoveryMNNetworkAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDiscoveryMNNetworkAddress.setStatus(_A)
class _CtDiscoveryMNIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtDiscoveryMNIndex_Type.__name__=_E
_CtDiscoveryMNIndex_Object=MibTableColumn
ctDiscoveryMNIndex=_CtDiscoveryMNIndex_Object((1,3,6,1,4,1,52,4,3,2,20,3,1,3),_CtDiscoveryMNIndex_Type())
ctDiscoveryMNIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDiscoveryMNIndex.setStatus(_A)
_CtDiscoveryMNCreationTime_Type=TimeTicks
_CtDiscoveryMNCreationTime_Object=MibTableColumn
ctDiscoveryMNCreationTime=_CtDiscoveryMNCreationTime_Object((1,3,6,1,4,1,52,4,3,2,20,3,1,4),_CtDiscoveryMNCreationTime_Type())
ctDiscoveryMNCreationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDiscoveryMNCreationTime.setStatus(_A)
_CtDiscoveryMNLastTransmitTime_Type=TimeTicks
_CtDiscoveryMNLastTransmitTime_Object=MibTableColumn
ctDiscoveryMNLastTransmitTime=_CtDiscoveryMNLastTransmitTime_Object((1,3,6,1,4,1,52,4,3,2,20,3,1,5),_CtDiscoveryMNLastTransmitTime_Type())
ctDiscoveryMNLastTransmitTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDiscoveryMNLastTransmitTime.setStatus(_A)
_CtDiscoveryMNBoard_Type=Integer32
_CtDiscoveryMNBoard_Object=MibTableColumn
ctDiscoveryMNBoard=_CtDiscoveryMNBoard_Object((1,3,6,1,4,1,52,4,3,2,20,3,1,6),_CtDiscoveryMNBoard_Type())
ctDiscoveryMNBoard.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDiscoveryMNBoard.setStatus(_A)
_CtDiscoveryMNPort_Type=Integer32
_CtDiscoveryMNPort_Object=MibTableColumn
ctDiscoveryMNPort=_CtDiscoveryMNPort_Object((1,3,6,1,4,1,52,4,3,2,20,3,1,7),_CtDiscoveryMNPort_Type())
ctDiscoveryMNPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDiscoveryMNPort.setStatus(_A)
_CtDiscoveryNMTable_Object=MibTable
ctDiscoveryNMTable=_CtDiscoveryNMTable_Object((1,3,6,1,4,1,52,4,3,2,20,4))
if mibBuilder.loadTexts:ctDiscoveryNMTable.setStatus(_A)
_CtDiscoveryNMEntry_Object=MibTableRow
ctDiscoveryNMEntry=_CtDiscoveryNMEntry_Object((1,3,6,1,4,1,52,4,3,2,20,4,1))
ctDiscoveryNMEntry.setIndexNames((0,_C,_J),(0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:ctDiscoveryNMEntry.setStatus(_A)
_CtDiscoveryNMNetworkAddress_Type=OctetString
_CtDiscoveryNMNetworkAddress_Object=MibTableColumn
ctDiscoveryNMNetworkAddress=_CtDiscoveryNMNetworkAddress_Object((1,3,6,1,4,1,52,4,3,2,20,4,1,1),_CtDiscoveryNMNetworkAddress_Type())
ctDiscoveryNMNetworkAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDiscoveryNMNetworkAddress.setStatus(_A)
_CtDiscoveryNMMACAddress_Type=OctetString
_CtDiscoveryNMMACAddress_Object=MibTableColumn
ctDiscoveryNMMACAddress=_CtDiscoveryNMMACAddress_Object((1,3,6,1,4,1,52,4,3,2,20,4,1,2),_CtDiscoveryNMMACAddress_Type())
ctDiscoveryNMMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDiscoveryNMMACAddress.setStatus(_A)
class _CtDiscoveryNMIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtDiscoveryNMIndex_Type.__name__=_E
_CtDiscoveryNMIndex_Object=MibTableColumn
ctDiscoveryNMIndex=_CtDiscoveryNMIndex_Object((1,3,6,1,4,1,52,4,3,2,20,4,1,3),_CtDiscoveryNMIndex_Type())
ctDiscoveryNMIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDiscoveryNMIndex.setStatus(_A)
_CtDiscoveryNMCreationTime_Type=TimeTicks
_CtDiscoveryNMCreationTime_Object=MibTableColumn
ctDiscoveryNMCreationTime=_CtDiscoveryNMCreationTime_Object((1,3,6,1,4,1,52,4,3,2,20,4,1,4),_CtDiscoveryNMCreationTime_Type())
ctDiscoveryNMCreationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDiscoveryNMCreationTime.setStatus(_A)
_CtDiscoveryNMLastTransmitTime_Type=TimeTicks
_CtDiscoveryNMLastTransmitTime_Object=MibTableColumn
ctDiscoveryNMLastTransmitTime=_CtDiscoveryNMLastTransmitTime_Object((1,3,6,1,4,1,52,4,3,2,20,4,1,5),_CtDiscoveryNMLastTransmitTime_Type())
ctDiscoveryNMLastTransmitTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDiscoveryNMLastTransmitTime.setStatus(_A)
_CtDiscoveryNMBoard_Type=Integer32
_CtDiscoveryNMBoard_Object=MibTableColumn
ctDiscoveryNMBoard=_CtDiscoveryNMBoard_Object((1,3,6,1,4,1,52,4,3,2,20,4,1,6),_CtDiscoveryNMBoard_Type())
ctDiscoveryNMBoard.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDiscoveryNMBoard.setStatus(_A)
_CtDiscoveryNMPort_Type=Integer32
_CtDiscoveryNMPort_Object=MibTableColumn
ctDiscoveryNMPort=_CtDiscoveryNMPort_Object((1,3,6,1,4,1,52,4,3,2,20,4,1,7),_CtDiscoveryNMPort_Type())
ctDiscoveryNMPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDiscoveryNMPort.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ctDiscovery':ctDiscovery,'ctDiscoveryProtocol':ctDiscoveryProtocol,'ctProtIP':ctProtIP,'ctProtNetware':ctProtNetware,'ctProtDecNet':ctProtDecNet,'ctDiscoveryControlTable':ctDiscoveryControlTable,'ctDiscoveryControlEntry':ctDiscoveryControlEntry,_F:ctDiscoveryControlIndex,'ctDiscoveryControlDataSource':ctDiscoveryControlDataSource,'ctDiscoveryControlProtocol':ctDiscoveryControlProtocol,'ctDiscoveryControlTableSize':ctDiscoveryControlTableSize,'ctDiscoveryControlLastDeleteTime':ctDiscoveryControlLastDeleteTime,'ctDiscoveryControlAgeInterval':ctDiscoveryControlAgeInterval,'ctDiscoveryControlOwner':ctDiscoveryControlOwner,'ctDiscoveryControlStatus':ctDiscoveryControlStatus,'ctDiscoveryMNTable':ctDiscoveryMNTable,'ctDiscoveryMNEntry':ctDiscoveryMNEntry,_H:ctDiscoveryMNMACAddress,_I:ctDiscoveryMNNetworkAddress,_G:ctDiscoveryMNIndex,'ctDiscoveryMNCreationTime':ctDiscoveryMNCreationTime,'ctDiscoveryMNLastTransmitTime':ctDiscoveryMNLastTransmitTime,'ctDiscoveryMNBoard':ctDiscoveryMNBoard,'ctDiscoveryMNPort':ctDiscoveryMNPort,'ctDiscoveryNMTable':ctDiscoveryNMTable,'ctDiscoveryNMEntry':ctDiscoveryNMEntry,_K:ctDiscoveryNMNetworkAddress,_L:ctDiscoveryNMMACAddress,_J:ctDiscoveryNMIndex,'ctDiscoveryNMCreationTime':ctDiscoveryNMCreationTime,'ctDiscoveryNMLastTransmitTime':ctDiscoveryNMLastTransmitTime,'ctDiscoveryNMBoard':ctDiscoveryNMBoard,'ctDiscoveryNMPort':ctDiscoveryNMPort})