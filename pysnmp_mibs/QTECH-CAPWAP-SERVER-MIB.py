_T='qtechCapwapSvrMIBGroup'
_S='qtechCapwapSvrBlackListPortRowStatus'
_R='qtechCapwapSvrBlackListIPRowStatus'
_Q='qtechCapwapSvrBlackListURLRowStatus'
_P='qtechCapwapSvrBlackListURLParserStatus'
_O='qtechCapwapSvrBlackListURL'
_N='qtechCapwapSvrWhiteListIPRowStatus'
_M='qtechCapwapSvrWhiteListURLRowStatus'
_L='qtechCapwapSvrWhiteListURLParserStatus'
_K='qtechCapwapSvrWhiteListURL'
_J='qtechCapwapSvrBlackListIndex'
_I='qtechCapwapSvrWhiteListIndex'
_H='qtechCapwapSvrBlackListPort'
_G='qtechCapwapSvrBlackListIP'
_F='qtechCapwapSvrWhiteListIP'
_E='DisplayString'
_D='read-create'
_C='read-only'
_B='QTECH-CAPWAP-SERVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
qtechCapwapSvrMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,89))
if mibBuilder.loadTexts:qtechCapwapSvrMIB.setRevisions(('2010-08-24 00:00',))
_QtechCapwapSvrMIBObjects_ObjectIdentity=ObjectIdentity
qtechCapwapSvrMIBObjects=_QtechCapwapSvrMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,89,1))
_QtechCapwapSvrWhiteListURLTable_Object=MibTable
qtechCapwapSvrWhiteListURLTable=_QtechCapwapSvrWhiteListURLTable_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,1))
if mibBuilder.loadTexts:qtechCapwapSvrWhiteListURLTable.setStatus(_A)
_QtechCapwapSvrWhiteListURLEntry_Object=MibTableRow
qtechCapwapSvrWhiteListURLEntry=_QtechCapwapSvrWhiteListURLEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,1,1))
qtechCapwapSvrWhiteListURLEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:qtechCapwapSvrWhiteListURLEntry.setStatus(_A)
_QtechCapwapSvrWhiteListIndex_Type=Unsigned32
_QtechCapwapSvrWhiteListIndex_Object=MibTableColumn
qtechCapwapSvrWhiteListIndex=_QtechCapwapSvrWhiteListIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,1,1,1),_QtechCapwapSvrWhiteListIndex_Type())
qtechCapwapSvrWhiteListIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCapwapSvrWhiteListIndex.setStatus(_A)
class _QtechCapwapSvrWhiteListURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechCapwapSvrWhiteListURL_Type.__name__=_E
_QtechCapwapSvrWhiteListURL_Object=MibTableColumn
qtechCapwapSvrWhiteListURL=_QtechCapwapSvrWhiteListURL_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,1,1,2),_QtechCapwapSvrWhiteListURL_Type())
qtechCapwapSvrWhiteListURL.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCapwapSvrWhiteListURL.setStatus(_A)
class _QtechCapwapSvrWhiteListURLParserStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechCapwapSvrWhiteListURLParserStatus_Type.__name__=_E
_QtechCapwapSvrWhiteListURLParserStatus_Object=MibTableColumn
qtechCapwapSvrWhiteListURLParserStatus=_QtechCapwapSvrWhiteListURLParserStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,1,1,3),_QtechCapwapSvrWhiteListURLParserStatus_Type())
qtechCapwapSvrWhiteListURLParserStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCapwapSvrWhiteListURLParserStatus.setStatus(_A)
_QtechCapwapSvrWhiteListURLRowStatus_Type=RowStatus
_QtechCapwapSvrWhiteListURLRowStatus_Object=MibTableColumn
qtechCapwapSvrWhiteListURLRowStatus=_QtechCapwapSvrWhiteListURLRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,1,1,4),_QtechCapwapSvrWhiteListURLRowStatus_Type())
qtechCapwapSvrWhiteListURLRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCapwapSvrWhiteListURLRowStatus.setStatus(_A)
_QtechCapwapSvrWhiteListIPTable_Object=MibTable
qtechCapwapSvrWhiteListIPTable=_QtechCapwapSvrWhiteListIPTable_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,2))
if mibBuilder.loadTexts:qtechCapwapSvrWhiteListIPTable.setStatus(_A)
_QtechCapwapSvrWhiteListIPEntry_Object=MibTableRow
qtechCapwapSvrWhiteListIPEntry=_QtechCapwapSvrWhiteListIPEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,2,1))
qtechCapwapSvrWhiteListIPEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:qtechCapwapSvrWhiteListIPEntry.setStatus(_A)
_QtechCapwapSvrWhiteListIP_Type=IpAddress
_QtechCapwapSvrWhiteListIP_Object=MibTableColumn
qtechCapwapSvrWhiteListIP=_QtechCapwapSvrWhiteListIP_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,2,1,1),_QtechCapwapSvrWhiteListIP_Type())
qtechCapwapSvrWhiteListIP.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCapwapSvrWhiteListIP.setStatus(_A)
_QtechCapwapSvrWhiteListIPRowStatus_Type=RowStatus
_QtechCapwapSvrWhiteListIPRowStatus_Object=MibTableColumn
qtechCapwapSvrWhiteListIPRowStatus=_QtechCapwapSvrWhiteListIPRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,2,1,2),_QtechCapwapSvrWhiteListIPRowStatus_Type())
qtechCapwapSvrWhiteListIPRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCapwapSvrWhiteListIPRowStatus.setStatus(_A)
_QtechCapwapSvrBlackListURLTable_Object=MibTable
qtechCapwapSvrBlackListURLTable=_QtechCapwapSvrBlackListURLTable_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,3))
if mibBuilder.loadTexts:qtechCapwapSvrBlackListURLTable.setStatus(_A)
_QtechCapwapSvrBlackListURLEntry_Object=MibTableRow
qtechCapwapSvrBlackListURLEntry=_QtechCapwapSvrBlackListURLEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,3,1))
qtechCapwapSvrBlackListURLEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:qtechCapwapSvrBlackListURLEntry.setStatus(_A)
_QtechCapwapSvrBlackListIndex_Type=Unsigned32
_QtechCapwapSvrBlackListIndex_Object=MibTableColumn
qtechCapwapSvrBlackListIndex=_QtechCapwapSvrBlackListIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,3,1,1),_QtechCapwapSvrBlackListIndex_Type())
qtechCapwapSvrBlackListIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCapwapSvrBlackListIndex.setStatus(_A)
class _QtechCapwapSvrBlackListURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechCapwapSvrBlackListURL_Type.__name__=_E
_QtechCapwapSvrBlackListURL_Object=MibTableColumn
qtechCapwapSvrBlackListURL=_QtechCapwapSvrBlackListURL_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,3,1,2),_QtechCapwapSvrBlackListURL_Type())
qtechCapwapSvrBlackListURL.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCapwapSvrBlackListURL.setStatus(_A)
class _QtechCapwapSvrBlackListURLParserStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechCapwapSvrBlackListURLParserStatus_Type.__name__=_E
_QtechCapwapSvrBlackListURLParserStatus_Object=MibTableColumn
qtechCapwapSvrBlackListURLParserStatus=_QtechCapwapSvrBlackListURLParserStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,3,1,3),_QtechCapwapSvrBlackListURLParserStatus_Type())
qtechCapwapSvrBlackListURLParserStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCapwapSvrBlackListURLParserStatus.setStatus(_A)
_QtechCapwapSvrBlackListURLRowStatus_Type=RowStatus
_QtechCapwapSvrBlackListURLRowStatus_Object=MibTableColumn
qtechCapwapSvrBlackListURLRowStatus=_QtechCapwapSvrBlackListURLRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,3,1,4),_QtechCapwapSvrBlackListURLRowStatus_Type())
qtechCapwapSvrBlackListURLRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCapwapSvrBlackListURLRowStatus.setStatus(_A)
_QtechCapwapSvrBlackListIPTable_Object=MibTable
qtechCapwapSvrBlackListIPTable=_QtechCapwapSvrBlackListIPTable_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,4))
if mibBuilder.loadTexts:qtechCapwapSvrBlackListIPTable.setStatus(_A)
_QtechCapwapSvrBlackListIPEntry_Object=MibTableRow
qtechCapwapSvrBlackListIPEntry=_QtechCapwapSvrBlackListIPEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,4,1))
qtechCapwapSvrBlackListIPEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:qtechCapwapSvrBlackListIPEntry.setStatus(_A)
_QtechCapwapSvrBlackListIP_Type=IpAddress
_QtechCapwapSvrBlackListIP_Object=MibTableColumn
qtechCapwapSvrBlackListIP=_QtechCapwapSvrBlackListIP_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,4,1,1),_QtechCapwapSvrBlackListIP_Type())
qtechCapwapSvrBlackListIP.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCapwapSvrBlackListIP.setStatus(_A)
_QtechCapwapSvrBlackListIPRowStatus_Type=RowStatus
_QtechCapwapSvrBlackListIPRowStatus_Object=MibTableColumn
qtechCapwapSvrBlackListIPRowStatus=_QtechCapwapSvrBlackListIPRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,4,1,2),_QtechCapwapSvrBlackListIPRowStatus_Type())
qtechCapwapSvrBlackListIPRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCapwapSvrBlackListIPRowStatus.setStatus(_A)
_QtechCapwapSvrBlackListPortTable_Object=MibTable
qtechCapwapSvrBlackListPortTable=_QtechCapwapSvrBlackListPortTable_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,5))
if mibBuilder.loadTexts:qtechCapwapSvrBlackListPortTable.setStatus(_A)
_QtechCapwapSvrBlackListPortEntry_Object=MibTableRow
qtechCapwapSvrBlackListPortEntry=_QtechCapwapSvrBlackListPortEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,5,1))
qtechCapwapSvrBlackListPortEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:qtechCapwapSvrBlackListPortEntry.setStatus(_A)
_QtechCapwapSvrBlackListPort_Type=Integer32
_QtechCapwapSvrBlackListPort_Object=MibTableColumn
qtechCapwapSvrBlackListPort=_QtechCapwapSvrBlackListPort_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,5,1,1),_QtechCapwapSvrBlackListPort_Type())
qtechCapwapSvrBlackListPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCapwapSvrBlackListPort.setStatus(_A)
_QtechCapwapSvrBlackListPortRowStatus_Type=RowStatus
_QtechCapwapSvrBlackListPortRowStatus_Object=MibTableColumn
qtechCapwapSvrBlackListPortRowStatus=_QtechCapwapSvrBlackListPortRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,89,1,5,1,2),_QtechCapwapSvrBlackListPortRowStatus_Type())
qtechCapwapSvrBlackListPortRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCapwapSvrBlackListPortRowStatus.setStatus(_A)
_QtechCapwapSvrMIBConformance_ObjectIdentity=ObjectIdentity
qtechCapwapSvrMIBConformance=_QtechCapwapSvrMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,89,2))
_QtechCapwapSvrMIBCompliances_ObjectIdentity=ObjectIdentity
qtechCapwapSvrMIBCompliances=_QtechCapwapSvrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,89,2,1))
_QtechCapwapSvrMIBGroups_ObjectIdentity=ObjectIdentity
qtechCapwapSvrMIBGroups=_QtechCapwapSvrMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,89,2,2))
qtechCapwapSvrMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,89,2,2,1))
qtechCapwapSvrMIBGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_F),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_G),(_B,_R),(_B,_H),(_B,_S)))
if mibBuilder.loadTexts:qtechCapwapSvrMIBGroup.setStatus('deprecated')
qtechCapwapSvrMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,89,2,1,1))
qtechCapwapSvrMIBCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:qtechCapwapSvrMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechCapwapSvrMIB':qtechCapwapSvrMIB,'qtechCapwapSvrMIBObjects':qtechCapwapSvrMIBObjects,'qtechCapwapSvrWhiteListURLTable':qtechCapwapSvrWhiteListURLTable,'qtechCapwapSvrWhiteListURLEntry':qtechCapwapSvrWhiteListURLEntry,_I:qtechCapwapSvrWhiteListIndex,_K:qtechCapwapSvrWhiteListURL,_L:qtechCapwapSvrWhiteListURLParserStatus,_M:qtechCapwapSvrWhiteListURLRowStatus,'qtechCapwapSvrWhiteListIPTable':qtechCapwapSvrWhiteListIPTable,'qtechCapwapSvrWhiteListIPEntry':qtechCapwapSvrWhiteListIPEntry,_F:qtechCapwapSvrWhiteListIP,_N:qtechCapwapSvrWhiteListIPRowStatus,'qtechCapwapSvrBlackListURLTable':qtechCapwapSvrBlackListURLTable,'qtechCapwapSvrBlackListURLEntry':qtechCapwapSvrBlackListURLEntry,_J:qtechCapwapSvrBlackListIndex,_O:qtechCapwapSvrBlackListURL,_P:qtechCapwapSvrBlackListURLParserStatus,_Q:qtechCapwapSvrBlackListURLRowStatus,'qtechCapwapSvrBlackListIPTable':qtechCapwapSvrBlackListIPTable,'qtechCapwapSvrBlackListIPEntry':qtechCapwapSvrBlackListIPEntry,_G:qtechCapwapSvrBlackListIP,_R:qtechCapwapSvrBlackListIPRowStatus,'qtechCapwapSvrBlackListPortTable':qtechCapwapSvrBlackListPortTable,'qtechCapwapSvrBlackListPortEntry':qtechCapwapSvrBlackListPortEntry,_H:qtechCapwapSvrBlackListPort,_S:qtechCapwapSvrBlackListPortRowStatus,'qtechCapwapSvrMIBConformance':qtechCapwapSvrMIBConformance,'qtechCapwapSvrMIBCompliances':qtechCapwapSvrMIBCompliances,'qtechCapwapSvrMIBCompliance':qtechCapwapSvrMIBCompliance,'qtechCapwapSvrMIBGroups':qtechCapwapSvrMIBGroups,_T:qtechCapwapSvrMIBGroup})