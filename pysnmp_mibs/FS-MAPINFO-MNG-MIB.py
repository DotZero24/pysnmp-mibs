_X='fsFluxMIBGroup'
_W='fsUserMIBGroup'
_V='fsFluxRowStatus'
_U='fsFluxOutputBytes'
_T='fsFluxInputBytes'
_S='fsFluxOutputPackets'
_R='fsFluxInputPackets'
_Q='fsFluxOutputBps'
_P='fsFluxInputBps'
_O='fsFluxMapPortState'
_N='fsUserRowStatus'
_M='fsUserMapPort'
_L='fsUserDevSlot'
_K='fsUserDevMacAddress'
_J='read-write'
_I='Integer32'
_H='fsFluxMapPort'
_G='fsFluxDevSlot'
_F='fsFluxDevMacAddress'
_E='fsUserVid'
_D='fsUserMacAddress'
_C='read-only'
_B='current'
_A='FS-MAPINFO-MNG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('FS-TC','ConfigStatus','IfIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
radiusAccClientServerPortNumber,radiusAccServerAddress=mibBuilder.importSymbols('RADIUS-ACC-CLIENT-MIB','radiusAccClientServerPortNumber','radiusAccServerAddress')
radiusAuthClientServerPortNumber,radiusAuthServerAddress=mibBuilder.importSymbols('RADIUS-AUTH-CLIENT-MIB','radiusAuthClientServerPortNumber','radiusAuthServerAddress')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsMapinfoMngMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,150))
if mibBuilder.loadTexts:fsMapinfoMngMIB.setRevisions(('2016-07-03 20:00',))
_FsMapinfoMngMIBObjects_ObjectIdentity=ObjectIdentity
fsMapinfoMngMIBObjects=_FsMapinfoMngMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,150,1))
_FsUserObjects_ObjectIdentity=ObjectIdentity
fsUserObjects=_FsUserObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,150,1,1))
_FsUserTable_Object=MibTable
fsUserTable=_FsUserTable_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,1,1))
if mibBuilder.loadTexts:fsUserTable.setStatus(_B)
_FsUserEntry_Object=MibTableRow
fsUserEntry=_FsUserEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,1,1,1))
fsUserEntry.setIndexNames((0,_A,_D),(0,_A,_E))
if mibBuilder.loadTexts:fsUserEntry.setStatus(_B)
_FsUserMacAddress_Type=MacAddress
_FsUserMacAddress_Object=MibTableColumn
fsUserMacAddress=_FsUserMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,1,1,1,1),_FsUserMacAddress_Type())
fsUserMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsUserMacAddress.setStatus(_B)
_FsUserVid_Type=Unsigned32
_FsUserVid_Object=MibTableColumn
fsUserVid=_FsUserVid_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,1,1,1,2),_FsUserVid_Type())
fsUserVid.setMaxAccess(_C)
if mibBuilder.loadTexts:fsUserVid.setStatus(_B)
_FsUserDevMacAddress_Type=MacAddress
_FsUserDevMacAddress_Object=MibTableColumn
fsUserDevMacAddress=_FsUserDevMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,1,1,1,3),_FsUserDevMacAddress_Type())
fsUserDevMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsUserDevMacAddress.setStatus(_B)
_FsUserDevSlot_Type=Unsigned32
_FsUserDevSlot_Object=MibTableColumn
fsUserDevSlot=_FsUserDevSlot_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,1,1,1,4),_FsUserDevSlot_Type())
fsUserDevSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:fsUserDevSlot.setStatus(_B)
_FsUserMapPort_Type=Unsigned32
_FsUserMapPort_Object=MibTableColumn
fsUserMapPort=_FsUserMapPort_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,1,1,1,5),_FsUserMapPort_Type())
fsUserMapPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsUserMapPort.setStatus(_B)
_FsUserRowStatus_Type=ConfigStatus
_FsUserRowStatus_Object=MibTableColumn
fsUserRowStatus=_FsUserRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,1,1,1,6),_FsUserRowStatus_Type())
fsUserRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:fsUserRowStatus.setStatus(_B)
_FsFluxObjects_ObjectIdentity=ObjectIdentity
fsFluxObjects=_FsFluxObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,150,1,2))
_FsFluxTable_Object=MibTable
fsFluxTable=_FsFluxTable_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,2,1))
if mibBuilder.loadTexts:fsFluxTable.setStatus(_B)
_FsFluxEntry_Object=MibTableRow
fsFluxEntry=_FsFluxEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,2,1,1))
fsFluxEntry.setIndexNames((0,_A,_F),(0,_A,_G),(0,_A,_H))
if mibBuilder.loadTexts:fsFluxEntry.setStatus(_B)
_FsFluxDevMacAddress_Type=MacAddress
_FsFluxDevMacAddress_Object=MibTableColumn
fsFluxDevMacAddress=_FsFluxDevMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,2,1,1,1),_FsFluxDevMacAddress_Type())
fsFluxDevMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFluxDevMacAddress.setStatus(_B)
_FsFluxDevSlot_Type=Unsigned32
_FsFluxDevSlot_Object=MibTableColumn
fsFluxDevSlot=_FsFluxDevSlot_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,2,1,1,2),_FsFluxDevSlot_Type())
fsFluxDevSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFluxDevSlot.setStatus(_B)
_FsFluxMapPort_Type=Unsigned32
_FsFluxMapPort_Object=MibTableColumn
fsFluxMapPort=_FsFluxMapPort_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,2,1,1,3),_FsFluxMapPort_Type())
fsFluxMapPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFluxMapPort.setStatus(_B)
class _FsFluxMapPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsFluxMapPortState_Type.__name__=_I
_FsFluxMapPortState_Object=MibTableColumn
fsFluxMapPortState=_FsFluxMapPortState_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,2,1,1,4),_FsFluxMapPortState_Type())
fsFluxMapPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFluxMapPortState.setStatus(_B)
_FsFluxInputBps_Type=Counter64
_FsFluxInputBps_Object=MibTableColumn
fsFluxInputBps=_FsFluxInputBps_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,2,1,1,5),_FsFluxInputBps_Type())
fsFluxInputBps.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFluxInputBps.setStatus(_B)
_FsFluxOutputBps_Type=Counter64
_FsFluxOutputBps_Object=MibTableColumn
fsFluxOutputBps=_FsFluxOutputBps_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,2,1,1,6),_FsFluxOutputBps_Type())
fsFluxOutputBps.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFluxOutputBps.setStatus(_B)
_FsFluxInputPackets_Type=Counter64
_FsFluxInputPackets_Object=MibTableColumn
fsFluxInputPackets=_FsFluxInputPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,2,1,1,7),_FsFluxInputPackets_Type())
fsFluxInputPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFluxInputPackets.setStatus(_B)
_FsFluxOutputPackets_Type=Counter64
_FsFluxOutputPackets_Object=MibTableColumn
fsFluxOutputPackets=_FsFluxOutputPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,2,1,1,8),_FsFluxOutputPackets_Type())
fsFluxOutputPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFluxOutputPackets.setStatus(_B)
_FsFluxInputBytes_Type=Counter64
_FsFluxInputBytes_Object=MibTableColumn
fsFluxInputBytes=_FsFluxInputBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,2,1,1,9),_FsFluxInputBytes_Type())
fsFluxInputBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFluxInputBytes.setStatus(_B)
_FsFluxOutputBytes_Type=Counter64
_FsFluxOutputBytes_Object=MibTableColumn
fsFluxOutputBytes=_FsFluxOutputBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,2,1,1,10),_FsFluxOutputBytes_Type())
fsFluxOutputBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFluxOutputBytes.setStatus(_B)
_FsFluxRowStatus_Type=ConfigStatus
_FsFluxRowStatus_Object=MibTableColumn
fsFluxRowStatus=_FsFluxRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,150,1,2,1,1,11),_FsFluxRowStatus_Type())
fsFluxRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:fsFluxRowStatus.setStatus(_B)
_FsMapinfoMngMIBConformance_ObjectIdentity=ObjectIdentity
fsMapinfoMngMIBConformance=_FsMapinfoMngMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,150,2))
_FsMapinfoMngMIBCompliances_ObjectIdentity=ObjectIdentity
fsMapinfoMngMIBCompliances=_FsMapinfoMngMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,150,2,1))
_FsMapinfoMngMIBGroups_ObjectIdentity=ObjectIdentity
fsMapinfoMngMIBGroups=_FsMapinfoMngMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,150,2,2))
fsUserMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,150,2,2,1))
fsUserMIBGroup.setObjects(*((_A,_D),(_A,_E),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:fsUserMIBGroup.setStatus(_B)
fsFluxMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,150,2,2,2))
fsFluxMIBGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:fsFluxMIBGroup.setStatus(_B)
fsMapinfoMngMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,150,2,1,1))
fsMapinfoMngMIBCompliance.setObjects(*((_A,_W),(_A,_X)))
if mibBuilder.loadTexts:fsMapinfoMngMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'fsMapinfoMngMIB':fsMapinfoMngMIB,'fsMapinfoMngMIBObjects':fsMapinfoMngMIBObjects,'fsUserObjects':fsUserObjects,'fsUserTable':fsUserTable,'fsUserEntry':fsUserEntry,_D:fsUserMacAddress,_E:fsUserVid,_K:fsUserDevMacAddress,_L:fsUserDevSlot,_M:fsUserMapPort,_N:fsUserRowStatus,'fsFluxObjects':fsFluxObjects,'fsFluxTable':fsFluxTable,'fsFluxEntry':fsFluxEntry,_F:fsFluxDevMacAddress,_G:fsFluxDevSlot,_H:fsFluxMapPort,_O:fsFluxMapPortState,_P:fsFluxInputBps,_Q:fsFluxOutputBps,_R:fsFluxInputPackets,_S:fsFluxOutputPackets,_T:fsFluxInputBytes,_U:fsFluxOutputBytes,_V:fsFluxRowStatus,'fsMapinfoMngMIBConformance':fsMapinfoMngMIBConformance,'fsMapinfoMngMIBCompliances':fsMapinfoMngMIBCompliances,'fsMapinfoMngMIBCompliance':fsMapinfoMngMIBCompliance,'fsMapinfoMngMIBGroups':fsMapinfoMngMIBGroups,_W:fsUserMIBGroup,_X:fsFluxMIBGroup})