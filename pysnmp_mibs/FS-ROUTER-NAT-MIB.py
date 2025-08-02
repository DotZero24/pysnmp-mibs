_I='fsNatInterfaceIndex'
_H='fsNatPoolAddressIndex'
_G='fsNatSettingIndex'
_F='read-only'
_E='FS-ROUTER-NAT-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsNatMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,136))
if mibBuilder.loadTexts:fsNatMIB.setRevisions(('2015-03-02 00:00',))
class FSNatType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inside',1),('outside',2),('application',3)))
class FSNatSrcDstType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('source',1),('destination',2)))
class FSNatTcpUdpType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tcp',1),('udp',2),('all',3)))
class FSNatPoolAddressntmskprefixFlag(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('netmask',1),('prefix-length',2)))
_FsNatMIBObjects_ObjectIdentity=ObjectIdentity
fsNatMIBObjects=_FsNatMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,136,1))
_FsNatSettingObjects_ObjectIdentity=ObjectIdentity
fsNatSettingObjects=_FsNatSettingObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,136,1,1))
_FsNatSettingTable_Object=MibTable
fsNatSettingTable=_FsNatSettingTable_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1))
if mibBuilder.loadTexts:fsNatSettingTable.setStatus(_A)
_FsNatSettingEntry_Object=MibTableRow
fsNatSettingEntry=_FsNatSettingEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1))
fsNatSettingEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:fsNatSettingEntry.setStatus(_A)
_FsNatSettingIndex_Type=Integer32
_FsNatSettingIndex_Object=MibTableColumn
fsNatSettingIndex=_FsNatSettingIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1,1),_FsNatSettingIndex_Type())
fsNatSettingIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsNatSettingIndex.setStatus(_A)
class _FsNatSettingisno_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsNatSettingisno_Type.__name__=_C
_FsNatSettingisno_Object=MibTableColumn
fsNatSettingisno=_FsNatSettingisno_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1,2),_FsNatSettingisno_Type())
fsNatSettingisno.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatSettingisno.setStatus(_A)
_FsNatSettingtype_Type=FSNatType
_FsNatSettingtype_Object=MibTableColumn
fsNatSettingtype=_FsNatSettingtype_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1,3),_FsNatSettingtype_Type())
fsNatSettingtype.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatSettingtype.setStatus(_A)
_FsNatSettingsrcdst_Type=FSNatSrcDstType
_FsNatSettingsrcdst_Object=MibTableColumn
fsNatSettingsrcdst=_FsNatSettingsrcdst_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1,4),_FsNatSettingsrcdst_Type())
fsNatSettingsrcdst.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatSettingsrcdst.setStatus(_A)
class _FsNatSettingacltype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsNatSettingacltype_Type.__name__=_C
_FsNatSettingacltype_Object=MibTableColumn
fsNatSettingacltype=_FsNatSettingacltype_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1,5),_FsNatSettingacltype_Type())
fsNatSettingacltype.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatSettingacltype.setStatus(_A)
_FsNatSettingaclnumber_Type=Integer32
_FsNatSettingaclnumber_Object=MibTableColumn
fsNatSettingaclnumber=_FsNatSettingaclnumber_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1,6),_FsNatSettingaclnumber_Type())
fsNatSettingaclnumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatSettingaclnumber.setStatus(_A)
class _FsNatSettingaclname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FsNatSettingaclname_Type.__name__=_D
_FsNatSettingaclname_Object=MibTableColumn
fsNatSettingaclname=_FsNatSettingaclname_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1,7),_FsNatSettingaclname_Type())
fsNatSettingaclname.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatSettingaclname.setStatus(_A)
class _FsNatSettingstaticrule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsNatSettingstaticrule_Type.__name__=_C
_FsNatSettingstaticrule_Object=MibTableColumn
fsNatSettingstaticrule=_FsNatSettingstaticrule_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1,8),_FsNatSettingstaticrule_Type())
fsNatSettingstaticrule.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatSettingstaticrule.setStatus(_A)
_FsNatSettingproto_Type=FSNatTcpUdpType
_FsNatSettingproto_Object=MibTableColumn
fsNatSettingproto=_FsNatSettingproto_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1,9),_FsNatSettingproto_Type())
fsNatSettingproto.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatSettingproto.setStatus(_A)
_FsNatSettinginlocalip_Type=IpAddress
_FsNatSettinginlocalip_Object=MibTableColumn
fsNatSettinginlocalip=_FsNatSettinginlocalip_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1,10),_FsNatSettinginlocalip_Type())
fsNatSettinginlocalip.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatSettinginlocalip.setStatus(_A)
_FsNatSettinginglobalip_Type=IpAddress
_FsNatSettinginglobalip_Object=MibTableColumn
fsNatSettinginglobalip=_FsNatSettinginglobalip_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1,11),_FsNatSettinginglobalip_Type())
fsNatSettinginglobalip.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatSettinginglobalip.setStatus(_A)
_FsNatSettingnetmask_Type=IpAddress
_FsNatSettingnetmask_Object=MibTableColumn
fsNatSettingnetmask=_FsNatSettingnetmask_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1,12),_FsNatSettingnetmask_Type())
fsNatSettingnetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatSettingnetmask.setStatus(_A)
_FsNatSettinglocalport_Type=Integer32
_FsNatSettinglocalport_Object=MibTableColumn
fsNatSettinglocalport=_FsNatSettinglocalport_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1,13),_FsNatSettinglocalport_Type())
fsNatSettinglocalport.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatSettinglocalport.setStatus(_A)
_FsNatSettingglobalport_Type=Integer32
_FsNatSettingglobalport_Object=MibTableColumn
fsNatSettingglobalport=_FsNatSettingglobalport_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1,14),_FsNatSettingglobalport_Type())
fsNatSettingglobalport.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatSettingglobalport.setStatus(_A)
_FsNatSettingmatchinterface_Type=Integer32
_FsNatSettingmatchinterface_Object=MibTableColumn
fsNatSettingmatchinterface=_FsNatSettingmatchinterface_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1,15),_FsNatSettingmatchinterface_Type())
fsNatSettingmatchinterface.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatSettingmatchinterface.setStatus(_A)
_FsNatSettingpermisinside_Type=Integer32
_FsNatSettingpermisinside_Object=MibTableColumn
fsNatSettingpermisinside=_FsNatSettingpermisinside_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1,16),_FsNatSettingpermisinside_Type())
fsNatSettingpermisinside.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatSettingpermisinside.setStatus(_A)
_FsNatSettinginterface_Type=Integer32
_FsNatSettinginterface_Object=MibTableColumn
fsNatSettinginterface=_FsNatSettinginterface_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1,17),_FsNatSettinginterface_Type())
fsNatSettinginterface.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatSettinginterface.setStatus(_A)
class _FsNatSettingpool_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FsNatSettingpool_Type.__name__=_D
_FsNatSettingpool_Object=MibTableColumn
fsNatSettingpool=_FsNatSettingpool_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1,18),_FsNatSettingpool_Type())
fsNatSettingpool.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatSettingpool.setStatus(_A)
_FsNatSettingdstchange_Type=IpAddress
_FsNatSettingdstchange_Object=MibTableColumn
fsNatSettingdstchange=_FsNatSettingdstchange_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1,19),_FsNatSettingdstchange_Type())
fsNatSettingdstchange.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatSettingdstchange.setStatus(_A)
_FsNatSettingsrcchange_Type=IpAddress
_FsNatSettingsrcchange_Object=MibTableColumn
fsNatSettingsrcchange=_FsNatSettingsrcchange_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,1,1,1,20),_FsNatSettingsrcchange_Type())
fsNatSettingsrcchange.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatSettingsrcchange.setStatus(_A)
_FsNatPoolAddressObjects_ObjectIdentity=ObjectIdentity
fsNatPoolAddressObjects=_FsNatPoolAddressObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,136,1,2))
_FsNatPoolAddressTable_Object=MibTable
fsNatPoolAddressTable=_FsNatPoolAddressTable_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,2,1))
if mibBuilder.loadTexts:fsNatPoolAddressTable.setStatus(_A)
_FsNatPoolAddressEntry_Object=MibTableRow
fsNatPoolAddressEntry=_FsNatPoolAddressEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,2,1,1))
fsNatPoolAddressEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:fsNatPoolAddressEntry.setStatus(_A)
_FsNatPoolAddressIndex_Type=Integer32
_FsNatPoolAddressIndex_Object=MibTableColumn
fsNatPoolAddressIndex=_FsNatPoolAddressIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,2,1,1,1),_FsNatPoolAddressIndex_Type())
fsNatPoolAddressIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsNatPoolAddressIndex.setStatus(_A)
class _FsNatPoolAddressisno_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsNatPoolAddressisno_Type.__name__=_C
_FsNatPoolAddressisno_Object=MibTableColumn
fsNatPoolAddressisno=_FsNatPoolAddressisno_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,2,1,1,2),_FsNatPoolAddressisno_Type())
fsNatPoolAddressisno.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatPoolAddressisno.setStatus(_A)
class _FsNatPoolAddressname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FsNatPoolAddressname_Type.__name__=_D
_FsNatPoolAddressname_Object=MibTableColumn
fsNatPoolAddressname=_FsNatPoolAddressname_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,2,1,1,3),_FsNatPoolAddressname_Type())
fsNatPoolAddressname.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatPoolAddressname.setStatus(_A)
_FsNatPoolAddressntmskprefix_Type=FSNatPoolAddressntmskprefixFlag
_FsNatPoolAddressntmskprefix_Object=MibTableColumn
fsNatPoolAddressntmskprefix=_FsNatPoolAddressntmskprefix_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,2,1,1,4),_FsNatPoolAddressntmskprefix_Type())
fsNatPoolAddressntmskprefix.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatPoolAddressntmskprefix.setStatus(_A)
_FsNatPoolAddressnetmask_Type=IpAddress
_FsNatPoolAddressnetmask_Object=MibTableColumn
fsNatPoolAddressnetmask=_FsNatPoolAddressnetmask_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,2,1,1,5),_FsNatPoolAddressnetmask_Type())
fsNatPoolAddressnetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatPoolAddressnetmask.setStatus(_A)
_FsNatPoolAddressprefixlength_Type=Integer32
_FsNatPoolAddressprefixlength_Object=MibTableColumn
fsNatPoolAddressprefixlength=_FsNatPoolAddressprefixlength_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,2,1,1,6),_FsNatPoolAddressprefixlength_Type())
fsNatPoolAddressprefixlength.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatPoolAddressprefixlength.setStatus(_A)
_FsNatPoolAddressstartip_Type=IpAddress
_FsNatPoolAddressstartip_Object=MibTableColumn
fsNatPoolAddressstartip=_FsNatPoolAddressstartip_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,2,1,1,7),_FsNatPoolAddressstartip_Type())
fsNatPoolAddressstartip.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatPoolAddressstartip.setStatus(_A)
_FsNatPoolAddressendip_Type=IpAddress
_FsNatPoolAddressendip_Object=MibTableColumn
fsNatPoolAddressendip=_FsNatPoolAddressendip_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,2,1,1,8),_FsNatPoolAddressendip_Type())
fsNatPoolAddressendip.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatPoolAddressendip.setStatus(_A)
_FsNatPoolAddressstartinterface_Type=Integer32
_FsNatPoolAddressstartinterface_Object=MibTableColumn
fsNatPoolAddressstartinterface=_FsNatPoolAddressstartinterface_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,2,1,1,9),_FsNatPoolAddressstartinterface_Type())
fsNatPoolAddressstartinterface.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatPoolAddressstartinterface.setStatus(_A)
_FsNatPoolAddressendinterface_Type=Integer32
_FsNatPoolAddressendinterface_Object=MibTableColumn
fsNatPoolAddressendinterface=_FsNatPoolAddressendinterface_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,2,1,1,10),_FsNatPoolAddressendinterface_Type())
fsNatPoolAddressendinterface.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatPoolAddressendinterface.setStatus(_A)
_FsNatPoolAddresstype_Type=Integer32
_FsNatPoolAddresstype_Object=MibTableColumn
fsNatPoolAddresstype=_FsNatPoolAddresstype_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,2,1,1,11),_FsNatPoolAddresstype_Type())
fsNatPoolAddresstype.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatPoolAddresstype.setStatus(_A)
_FsNatInterfaceObjects_ObjectIdentity=ObjectIdentity
fsNatInterfaceObjects=_FsNatInterfaceObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,136,1,3))
_FsNatInterfaceTable_Object=MibTable
fsNatInterfaceTable=_FsNatInterfaceTable_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,3,1))
if mibBuilder.loadTexts:fsNatInterfaceTable.setStatus(_A)
_FsNatInterfaceEntry_Object=MibTableRow
fsNatInterfaceEntry=_FsNatInterfaceEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,3,1,1))
fsNatInterfaceEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:fsNatInterfaceEntry.setStatus(_A)
_FsNatInterfaceIndex_Type=Integer32
_FsNatInterfaceIndex_Object=MibTableColumn
fsNatInterfaceIndex=_FsNatInterfaceIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,3,1,1,1),_FsNatInterfaceIndex_Type())
fsNatInterfaceIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsNatInterfaceIndex.setStatus(_A)
class _FsNatInterfaceisno_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsNatInterfaceisno_Type.__name__=_C
_FsNatInterfaceisno_Object=MibTableColumn
fsNatInterfaceisno=_FsNatInterfaceisno_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,3,1,1,2),_FsNatInterfaceisno_Type())
fsNatInterfaceisno.setMaxAccess(_F)
if mibBuilder.loadTexts:fsNatInterfaceisno.setStatus(_A)
_FsNatInterfacedirector_Type=Integer32
_FsNatInterfacedirector_Object=MibTableColumn
fsNatInterfacedirector=_FsNatInterfacedirector_Object((1,3,6,1,4,1,52642,1,1,10,2,136,1,3,1,1,3),_FsNatInterfacedirector_Type())
fsNatInterfacedirector.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNatInterfacedirector.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'FSNatType':FSNatType,'FSNatSrcDstType':FSNatSrcDstType,'FSNatTcpUdpType':FSNatTcpUdpType,'FSNatPoolAddressntmskprefixFlag':FSNatPoolAddressntmskprefixFlag,'fsNatMIB':fsNatMIB,'fsNatMIBObjects':fsNatMIBObjects,'fsNatSettingObjects':fsNatSettingObjects,'fsNatSettingTable':fsNatSettingTable,'fsNatSettingEntry':fsNatSettingEntry,_G:fsNatSettingIndex,'fsNatSettingisno':fsNatSettingisno,'fsNatSettingtype':fsNatSettingtype,'fsNatSettingsrcdst':fsNatSettingsrcdst,'fsNatSettingacltype':fsNatSettingacltype,'fsNatSettingaclnumber':fsNatSettingaclnumber,'fsNatSettingaclname':fsNatSettingaclname,'fsNatSettingstaticrule':fsNatSettingstaticrule,'fsNatSettingproto':fsNatSettingproto,'fsNatSettinginlocalip':fsNatSettinginlocalip,'fsNatSettinginglobalip':fsNatSettinginglobalip,'fsNatSettingnetmask':fsNatSettingnetmask,'fsNatSettinglocalport':fsNatSettinglocalport,'fsNatSettingglobalport':fsNatSettingglobalport,'fsNatSettingmatchinterface':fsNatSettingmatchinterface,'fsNatSettingpermisinside':fsNatSettingpermisinside,'fsNatSettinginterface':fsNatSettinginterface,'fsNatSettingpool':fsNatSettingpool,'fsNatSettingdstchange':fsNatSettingdstchange,'fsNatSettingsrcchange':fsNatSettingsrcchange,'fsNatPoolAddressObjects':fsNatPoolAddressObjects,'fsNatPoolAddressTable':fsNatPoolAddressTable,'fsNatPoolAddressEntry':fsNatPoolAddressEntry,_H:fsNatPoolAddressIndex,'fsNatPoolAddressisno':fsNatPoolAddressisno,'fsNatPoolAddressname':fsNatPoolAddressname,'fsNatPoolAddressntmskprefix':fsNatPoolAddressntmskprefix,'fsNatPoolAddressnetmask':fsNatPoolAddressnetmask,'fsNatPoolAddressprefixlength':fsNatPoolAddressprefixlength,'fsNatPoolAddressstartip':fsNatPoolAddressstartip,'fsNatPoolAddressendip':fsNatPoolAddressendip,'fsNatPoolAddressstartinterface':fsNatPoolAddressstartinterface,'fsNatPoolAddressendinterface':fsNatPoolAddressendinterface,'fsNatPoolAddresstype':fsNatPoolAddresstype,'fsNatInterfaceObjects':fsNatInterfaceObjects,'fsNatInterfaceTable':fsNatInterfaceTable,'fsNatInterfaceEntry':fsNatInterfaceEntry,_I:fsNatInterfaceIndex,'fsNatInterfaceisno':fsNatInterfaceisno,'fsNatInterfacedirector':fsNatInterfacedirector})