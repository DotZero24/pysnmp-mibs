_W='fsCapwapSvrMIBGroup'
_V='fsCapwapSvrWhiteListMacRowStatus'
_U='fsCapwapSvrWhiteListMac'
_T='fsCapwapSvrBlackListPortRowStatus'
_S='fsCapwapSvrBlackListIPRowStatus'
_R='fsCapwapSvrBlackListURLRowStatus'
_Q='fsCapwapSvrBlackListURLParserStatus'
_P='fsCapwapSvrBlackListURL'
_O='fsCapwapSvrWhiteListIPRowStatus'
_N='fsCapwapSvrWhiteListURLRowStatus'
_M='fsCapwapSvrWhiteListURLParserStatus'
_L='fsCapwapSvrWhiteListURL'
_K='fsCapwapSvrWhiteListMacIndex'
_J='fsCapwapSvrBlackListIndex'
_I='fsCapwapSvrWhiteListIndex'
_H='fsCapwapSvrBlackListPort'
_G='fsCapwapSvrBlackListIP'
_F='fsCapwapSvrWhiteListIP'
_E='DisplayString'
_D='read-only'
_C='read-create'
_B='FS-CAPWAP-SERVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','RowStatus','TextualConvention')
fsCapwapSvrMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,89))
if mibBuilder.loadTexts:fsCapwapSvrMIB.setRevisions(('2010-08-24 00:00',))
_FsCapwapSvrMIBObjects_ObjectIdentity=ObjectIdentity
fsCapwapSvrMIBObjects=_FsCapwapSvrMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,89,1))
_FsCapwapSvrWhiteListURLTable_Object=MibTable
fsCapwapSvrWhiteListURLTable=_FsCapwapSvrWhiteListURLTable_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,1))
if mibBuilder.loadTexts:fsCapwapSvrWhiteListURLTable.setStatus(_A)
_FsCapwapSvrWhiteListURLEntry_Object=MibTableRow
fsCapwapSvrWhiteListURLEntry=_FsCapwapSvrWhiteListURLEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,1,1))
fsCapwapSvrWhiteListURLEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:fsCapwapSvrWhiteListURLEntry.setStatus(_A)
_FsCapwapSvrWhiteListIndex_Type=Unsigned32
_FsCapwapSvrWhiteListIndex_Object=MibTableColumn
fsCapwapSvrWhiteListIndex=_FsCapwapSvrWhiteListIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,1,1,1),_FsCapwapSvrWhiteListIndex_Type())
fsCapwapSvrWhiteListIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCapwapSvrWhiteListIndex.setStatus(_A)
class _FsCapwapSvrWhiteListURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsCapwapSvrWhiteListURL_Type.__name__=_E
_FsCapwapSvrWhiteListURL_Object=MibTableColumn
fsCapwapSvrWhiteListURL=_FsCapwapSvrWhiteListURL_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,1,1,2),_FsCapwapSvrWhiteListURL_Type())
fsCapwapSvrWhiteListURL.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCapwapSvrWhiteListURL.setStatus(_A)
class _FsCapwapSvrWhiteListURLParserStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsCapwapSvrWhiteListURLParserStatus_Type.__name__=_E
_FsCapwapSvrWhiteListURLParserStatus_Object=MibTableColumn
fsCapwapSvrWhiteListURLParserStatus=_FsCapwapSvrWhiteListURLParserStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,1,1,3),_FsCapwapSvrWhiteListURLParserStatus_Type())
fsCapwapSvrWhiteListURLParserStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCapwapSvrWhiteListURLParserStatus.setStatus(_A)
_FsCapwapSvrWhiteListURLRowStatus_Type=RowStatus
_FsCapwapSvrWhiteListURLRowStatus_Object=MibTableColumn
fsCapwapSvrWhiteListURLRowStatus=_FsCapwapSvrWhiteListURLRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,1,1,4),_FsCapwapSvrWhiteListURLRowStatus_Type())
fsCapwapSvrWhiteListURLRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCapwapSvrWhiteListURLRowStatus.setStatus(_A)
_FsCapwapSvrWhiteListIPTable_Object=MibTable
fsCapwapSvrWhiteListIPTable=_FsCapwapSvrWhiteListIPTable_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,2))
if mibBuilder.loadTexts:fsCapwapSvrWhiteListIPTable.setStatus(_A)
_FsCapwapSvrWhiteListIPEntry_Object=MibTableRow
fsCapwapSvrWhiteListIPEntry=_FsCapwapSvrWhiteListIPEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,2,1))
fsCapwapSvrWhiteListIPEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:fsCapwapSvrWhiteListIPEntry.setStatus(_A)
_FsCapwapSvrWhiteListIP_Type=IpAddress
_FsCapwapSvrWhiteListIP_Object=MibTableColumn
fsCapwapSvrWhiteListIP=_FsCapwapSvrWhiteListIP_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,2,1,1),_FsCapwapSvrWhiteListIP_Type())
fsCapwapSvrWhiteListIP.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCapwapSvrWhiteListIP.setStatus(_A)
_FsCapwapSvrWhiteListIPRowStatus_Type=RowStatus
_FsCapwapSvrWhiteListIPRowStatus_Object=MibTableColumn
fsCapwapSvrWhiteListIPRowStatus=_FsCapwapSvrWhiteListIPRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,2,1,2),_FsCapwapSvrWhiteListIPRowStatus_Type())
fsCapwapSvrWhiteListIPRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCapwapSvrWhiteListIPRowStatus.setStatus(_A)
_FsCapwapSvrBlackListURLTable_Object=MibTable
fsCapwapSvrBlackListURLTable=_FsCapwapSvrBlackListURLTable_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,3))
if mibBuilder.loadTexts:fsCapwapSvrBlackListURLTable.setStatus(_A)
_FsCapwapSvrBlackListURLEntry_Object=MibTableRow
fsCapwapSvrBlackListURLEntry=_FsCapwapSvrBlackListURLEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,3,1))
fsCapwapSvrBlackListURLEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:fsCapwapSvrBlackListURLEntry.setStatus(_A)
_FsCapwapSvrBlackListIndex_Type=Unsigned32
_FsCapwapSvrBlackListIndex_Object=MibTableColumn
fsCapwapSvrBlackListIndex=_FsCapwapSvrBlackListIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,3,1,1),_FsCapwapSvrBlackListIndex_Type())
fsCapwapSvrBlackListIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCapwapSvrBlackListIndex.setStatus(_A)
class _FsCapwapSvrBlackListURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsCapwapSvrBlackListURL_Type.__name__=_E
_FsCapwapSvrBlackListURL_Object=MibTableColumn
fsCapwapSvrBlackListURL=_FsCapwapSvrBlackListURL_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,3,1,2),_FsCapwapSvrBlackListURL_Type())
fsCapwapSvrBlackListURL.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCapwapSvrBlackListURL.setStatus(_A)
class _FsCapwapSvrBlackListURLParserStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsCapwapSvrBlackListURLParserStatus_Type.__name__=_E
_FsCapwapSvrBlackListURLParserStatus_Object=MibTableColumn
fsCapwapSvrBlackListURLParserStatus=_FsCapwapSvrBlackListURLParserStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,3,1,3),_FsCapwapSvrBlackListURLParserStatus_Type())
fsCapwapSvrBlackListURLParserStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCapwapSvrBlackListURLParserStatus.setStatus(_A)
_FsCapwapSvrBlackListURLRowStatus_Type=RowStatus
_FsCapwapSvrBlackListURLRowStatus_Object=MibTableColumn
fsCapwapSvrBlackListURLRowStatus=_FsCapwapSvrBlackListURLRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,3,1,4),_FsCapwapSvrBlackListURLRowStatus_Type())
fsCapwapSvrBlackListURLRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCapwapSvrBlackListURLRowStatus.setStatus(_A)
_FsCapwapSvrBlackListIPTable_Object=MibTable
fsCapwapSvrBlackListIPTable=_FsCapwapSvrBlackListIPTable_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,4))
if mibBuilder.loadTexts:fsCapwapSvrBlackListIPTable.setStatus(_A)
_FsCapwapSvrBlackListIPEntry_Object=MibTableRow
fsCapwapSvrBlackListIPEntry=_FsCapwapSvrBlackListIPEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,4,1))
fsCapwapSvrBlackListIPEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:fsCapwapSvrBlackListIPEntry.setStatus(_A)
_FsCapwapSvrBlackListIP_Type=IpAddress
_FsCapwapSvrBlackListIP_Object=MibTableColumn
fsCapwapSvrBlackListIP=_FsCapwapSvrBlackListIP_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,4,1,1),_FsCapwapSvrBlackListIP_Type())
fsCapwapSvrBlackListIP.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCapwapSvrBlackListIP.setStatus(_A)
_FsCapwapSvrBlackListIPRowStatus_Type=RowStatus
_FsCapwapSvrBlackListIPRowStatus_Object=MibTableColumn
fsCapwapSvrBlackListIPRowStatus=_FsCapwapSvrBlackListIPRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,4,1,2),_FsCapwapSvrBlackListIPRowStatus_Type())
fsCapwapSvrBlackListIPRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCapwapSvrBlackListIPRowStatus.setStatus(_A)
_FsCapwapSvrBlackListPortTable_Object=MibTable
fsCapwapSvrBlackListPortTable=_FsCapwapSvrBlackListPortTable_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,5))
if mibBuilder.loadTexts:fsCapwapSvrBlackListPortTable.setStatus(_A)
_FsCapwapSvrBlackListPortEntry_Object=MibTableRow
fsCapwapSvrBlackListPortEntry=_FsCapwapSvrBlackListPortEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,5,1))
fsCapwapSvrBlackListPortEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:fsCapwapSvrBlackListPortEntry.setStatus(_A)
_FsCapwapSvrBlackListPort_Type=Integer32
_FsCapwapSvrBlackListPort_Object=MibTableColumn
fsCapwapSvrBlackListPort=_FsCapwapSvrBlackListPort_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,5,1,1),_FsCapwapSvrBlackListPort_Type())
fsCapwapSvrBlackListPort.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCapwapSvrBlackListPort.setStatus(_A)
_FsCapwapSvrBlackListPortRowStatus_Type=RowStatus
_FsCapwapSvrBlackListPortRowStatus_Object=MibTableColumn
fsCapwapSvrBlackListPortRowStatus=_FsCapwapSvrBlackListPortRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,5,1,2),_FsCapwapSvrBlackListPortRowStatus_Type())
fsCapwapSvrBlackListPortRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCapwapSvrBlackListPortRowStatus.setStatus(_A)
_FsCapwapSvrWhiteListMacTable_Object=MibTable
fsCapwapSvrWhiteListMacTable=_FsCapwapSvrWhiteListMacTable_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,6))
if mibBuilder.loadTexts:fsCapwapSvrWhiteListMacTable.setStatus(_A)
_FsCapwapSvrWhiteListMacEntry_Object=MibTableRow
fsCapwapSvrWhiteListMacEntry=_FsCapwapSvrWhiteListMacEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,6,1))
fsCapwapSvrWhiteListMacEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:fsCapwapSvrWhiteListMacEntry.setStatus(_A)
_FsCapwapSvrWhiteListMacIndex_Type=Unsigned32
_FsCapwapSvrWhiteListMacIndex_Object=MibTableColumn
fsCapwapSvrWhiteListMacIndex=_FsCapwapSvrWhiteListMacIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,6,1,1),_FsCapwapSvrWhiteListMacIndex_Type())
fsCapwapSvrWhiteListMacIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCapwapSvrWhiteListMacIndex.setStatus(_A)
_FsCapwapSvrWhiteListMac_Type=MacAddress
_FsCapwapSvrWhiteListMac_Object=MibTableColumn
fsCapwapSvrWhiteListMac=_FsCapwapSvrWhiteListMac_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,6,1,2),_FsCapwapSvrWhiteListMac_Type())
fsCapwapSvrWhiteListMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCapwapSvrWhiteListMac.setStatus(_A)
_FsCapwapSvrWhiteListMacRowStatus_Type=RowStatus
_FsCapwapSvrWhiteListMacRowStatus_Object=MibTableColumn
fsCapwapSvrWhiteListMacRowStatus=_FsCapwapSvrWhiteListMacRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,89,1,6,1,3),_FsCapwapSvrWhiteListMacRowStatus_Type())
fsCapwapSvrWhiteListMacRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCapwapSvrWhiteListMacRowStatus.setStatus(_A)
_FsCapwapSvrMIBConformance_ObjectIdentity=ObjectIdentity
fsCapwapSvrMIBConformance=_FsCapwapSvrMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,89,2))
_FsCapwapSvrMIBCompliances_ObjectIdentity=ObjectIdentity
fsCapwapSvrMIBCompliances=_FsCapwapSvrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,89,2,1))
_FsCapwapSvrMIBGroups_ObjectIdentity=ObjectIdentity
fsCapwapSvrMIBGroups=_FsCapwapSvrMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,89,2,2))
fsCapwapSvrMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,89,2,2,1))
fsCapwapSvrMIBGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_F),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_G),(_B,_S),(_B,_H),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:fsCapwapSvrMIBGroup.setStatus('deprecated')
fsCapwapSvrMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,89,2,1,1))
fsCapwapSvrMIBCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:fsCapwapSvrMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsCapwapSvrMIB':fsCapwapSvrMIB,'fsCapwapSvrMIBObjects':fsCapwapSvrMIBObjects,'fsCapwapSvrWhiteListURLTable':fsCapwapSvrWhiteListURLTable,'fsCapwapSvrWhiteListURLEntry':fsCapwapSvrWhiteListURLEntry,_I:fsCapwapSvrWhiteListIndex,_L:fsCapwapSvrWhiteListURL,_M:fsCapwapSvrWhiteListURLParserStatus,_N:fsCapwapSvrWhiteListURLRowStatus,'fsCapwapSvrWhiteListIPTable':fsCapwapSvrWhiteListIPTable,'fsCapwapSvrWhiteListIPEntry':fsCapwapSvrWhiteListIPEntry,_F:fsCapwapSvrWhiteListIP,_O:fsCapwapSvrWhiteListIPRowStatus,'fsCapwapSvrBlackListURLTable':fsCapwapSvrBlackListURLTable,'fsCapwapSvrBlackListURLEntry':fsCapwapSvrBlackListURLEntry,_J:fsCapwapSvrBlackListIndex,_P:fsCapwapSvrBlackListURL,_Q:fsCapwapSvrBlackListURLParserStatus,_R:fsCapwapSvrBlackListURLRowStatus,'fsCapwapSvrBlackListIPTable':fsCapwapSvrBlackListIPTable,'fsCapwapSvrBlackListIPEntry':fsCapwapSvrBlackListIPEntry,_G:fsCapwapSvrBlackListIP,_S:fsCapwapSvrBlackListIPRowStatus,'fsCapwapSvrBlackListPortTable':fsCapwapSvrBlackListPortTable,'fsCapwapSvrBlackListPortEntry':fsCapwapSvrBlackListPortEntry,_H:fsCapwapSvrBlackListPort,_T:fsCapwapSvrBlackListPortRowStatus,'fsCapwapSvrWhiteListMacTable':fsCapwapSvrWhiteListMacTable,'fsCapwapSvrWhiteListMacEntry':fsCapwapSvrWhiteListMacEntry,_K:fsCapwapSvrWhiteListMacIndex,_U:fsCapwapSvrWhiteListMac,_V:fsCapwapSvrWhiteListMacRowStatus,'fsCapwapSvrMIBConformance':fsCapwapSvrMIBConformance,'fsCapwapSvrMIBCompliances':fsCapwapSvrMIBCompliances,'fsCapwapSvrMIBCompliance':fsCapwapSvrMIBCompliance,'fsCapwapSvrMIBGroups':fsCapwapSvrMIBGroups,_W:fsCapwapSvrMIBGroup})