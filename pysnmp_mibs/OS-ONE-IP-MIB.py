_a='osOneIpMngNatMandatoryGroup'
_Z='osOneIpMngCfgAdminStatus'
_Y='osOneIpMngCfgOperStatus'
_X='osOneIpMngCfgAltLastPort'
_W='osOneIpMngCfgAltFirstPort'
_V='osOneIpMngCfgStdLastPort'
_U='osOneIpMngCfgStdFirstPort'
_T='osOneIpMngCfgListType'
_S='osOneIpMngCfgTransport'
_R='osOneIpMngDefOperStatus'
_Q='osOneIpMngDefAltLastPort'
_P='osOneIpMngDefAltFirstPort'
_O='osOneIpMngDefStdLastPort'
_N='osOneIpMngDefStdFirstPort'
_M='osOneIpMngDefListType'
_L='osOneIpMngDefTransport'
_K='osOneIpManagFeatOpStatus'
_J='osOneIpMngCfgName'
_I='single'
_H='not-accessible'
_G='osOneIpMngDefName'
_F='read-write'
_E='read-only'
_D='Unsigned32'
_C='Integer32'
_B='OS-ONE-IP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EntityName,oaOptiSwitch=mibBuilder.importSymbols('OS-COMMON-TC-MIB','EntityName','oaOptiSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
osOneIpMng=ModuleIdentity((1,3,6,1,4,1,6926,2,43))
if mibBuilder.loadTexts:osOneIpMng.setRevisions(('2014-10-15 00:00',))
_OsOneIpMngNat_ObjectIdentity=ObjectIdentity
osOneIpMngNat=_OsOneIpMngNat_ObjectIdentity((1,3,6,1,4,1,6926,2,43,1))
_OsOneIpMngNatGen_ObjectIdentity=ObjectIdentity
osOneIpMngNatGen=_OsOneIpMngNatGen_ObjectIdentity((1,3,6,1,4,1,6926,2,43,1,1))
_OsOneIpMngDefaultTable_Object=MibTable
osOneIpMngDefaultTable=_OsOneIpMngDefaultTable_Object((1,3,6,1,4,1,6926,2,43,1,1,2))
if mibBuilder.loadTexts:osOneIpMngDefaultTable.setStatus(_A)
_OsOneIpMngDefaultEntry_Object=MibTableRow
osOneIpMngDefaultEntry=_OsOneIpMngDefaultEntry_Object((1,3,6,1,4,1,6926,2,43,1,1,2,1))
osOneIpMngDefaultEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:osOneIpMngDefaultEntry.setStatus(_A)
_OsOneIpMngDefName_Type=EntityName
_OsOneIpMngDefName_Object=MibTableColumn
osOneIpMngDefName=_OsOneIpMngDefName_Object((1,3,6,1,4,1,6926,2,43,1,1,2,1,1),_OsOneIpMngDefName_Type())
osOneIpMngDefName.setMaxAccess(_H)
if mibBuilder.loadTexts:osOneIpMngDefName.setStatus(_A)
class _OsOneIpMngDefTransport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,17)));namedValues=NamedValues(*(('tcp',6),('udp',17)))
_OsOneIpMngDefTransport_Type.__name__=_C
_OsOneIpMngDefTransport_Object=MibTableColumn
osOneIpMngDefTransport=_OsOneIpMngDefTransport_Object((1,3,6,1,4,1,6926,2,43,1,1,2,1,2),_OsOneIpMngDefTransport_Type())
osOneIpMngDefTransport.setMaxAccess(_E)
if mibBuilder.loadTexts:osOneIpMngDefTransport.setStatus(_A)
class _OsOneIpMngDefListType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('range',2),('pair',3)))
_OsOneIpMngDefListType_Type.__name__=_C
_OsOneIpMngDefListType_Object=MibTableColumn
osOneIpMngDefListType=_OsOneIpMngDefListType_Object((1,3,6,1,4,1,6926,2,43,1,1,2,1,3),_OsOneIpMngDefListType_Type())
osOneIpMngDefListType.setMaxAccess(_E)
if mibBuilder.loadTexts:osOneIpMngDefListType.setStatus(_A)
class _OsOneIpMngDefStdFirstPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OsOneIpMngDefStdFirstPort_Type.__name__=_D
_OsOneIpMngDefStdFirstPort_Object=MibTableColumn
osOneIpMngDefStdFirstPort=_OsOneIpMngDefStdFirstPort_Object((1,3,6,1,4,1,6926,2,43,1,1,2,1,4),_OsOneIpMngDefStdFirstPort_Type())
osOneIpMngDefStdFirstPort.setMaxAccess(_E)
if mibBuilder.loadTexts:osOneIpMngDefStdFirstPort.setStatus(_A)
class _OsOneIpMngDefStdLastPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OsOneIpMngDefStdLastPort_Type.__name__=_D
_OsOneIpMngDefStdLastPort_Object=MibTableColumn
osOneIpMngDefStdLastPort=_OsOneIpMngDefStdLastPort_Object((1,3,6,1,4,1,6926,2,43,1,1,2,1,5),_OsOneIpMngDefStdLastPort_Type())
osOneIpMngDefStdLastPort.setMaxAccess(_E)
if mibBuilder.loadTexts:osOneIpMngDefStdLastPort.setStatus(_A)
class _OsOneIpMngDefAltFirstPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OsOneIpMngDefAltFirstPort_Type.__name__=_D
_OsOneIpMngDefAltFirstPort_Object=MibTableColumn
osOneIpMngDefAltFirstPort=_OsOneIpMngDefAltFirstPort_Object((1,3,6,1,4,1,6926,2,43,1,1,2,1,6),_OsOneIpMngDefAltFirstPort_Type())
osOneIpMngDefAltFirstPort.setMaxAccess(_E)
if mibBuilder.loadTexts:osOneIpMngDefAltFirstPort.setStatus(_A)
class _OsOneIpMngDefAltLastPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OsOneIpMngDefAltLastPort_Type.__name__=_D
_OsOneIpMngDefAltLastPort_Object=MibTableColumn
osOneIpMngDefAltLastPort=_OsOneIpMngDefAltLastPort_Object((1,3,6,1,4,1,6926,2,43,1,1,2,1,7),_OsOneIpMngDefAltLastPort_Type())
osOneIpMngDefAltLastPort.setMaxAccess(_E)
if mibBuilder.loadTexts:osOneIpMngDefAltLastPort.setStatus(_A)
class _OsOneIpMngDefOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('original',1),('modified',2),('removed',3)))
_OsOneIpMngDefOperStatus_Type.__name__=_C
_OsOneIpMngDefOperStatus_Object=MibTableColumn
osOneIpMngDefOperStatus=_OsOneIpMngDefOperStatus_Object((1,3,6,1,4,1,6926,2,43,1,1,2,1,98),_OsOneIpMngDefOperStatus_Type())
osOneIpMngDefOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:osOneIpMngDefOperStatus.setStatus(_A)
_OsOneIpMngProtoTable_Object=MibTable
osOneIpMngProtoTable=_OsOneIpMngProtoTable_Object((1,3,6,1,4,1,6926,2,43,1,1,3))
if mibBuilder.loadTexts:osOneIpMngProtoTable.setStatus(_A)
_OsOneIpMngProtoEntry_Object=MibTableRow
osOneIpMngProtoEntry=_OsOneIpMngProtoEntry_Object((1,3,6,1,4,1,6926,2,43,1,1,3,1))
osOneIpMngProtoEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:osOneIpMngProtoEntry.setStatus(_A)
_OsOneIpMngCfgName_Type=EntityName
_OsOneIpMngCfgName_Object=MibTableColumn
osOneIpMngCfgName=_OsOneIpMngCfgName_Object((1,3,6,1,4,1,6926,2,43,1,1,3,1,1),_OsOneIpMngCfgName_Type())
osOneIpMngCfgName.setMaxAccess(_H)
if mibBuilder.loadTexts:osOneIpMngCfgName.setStatus(_A)
class _OsOneIpMngCfgTransport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,17)));namedValues=NamedValues(*(('tcp',6),('udp',17)))
_OsOneIpMngCfgTransport_Type.__name__=_C
_OsOneIpMngCfgTransport_Object=MibTableColumn
osOneIpMngCfgTransport=_OsOneIpMngCfgTransport_Object((1,3,6,1,4,1,6926,2,43,1,1,3,1,2),_OsOneIpMngCfgTransport_Type())
osOneIpMngCfgTransport.setMaxAccess(_F)
if mibBuilder.loadTexts:osOneIpMngCfgTransport.setStatus(_A)
class _OsOneIpMngCfgListType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('range',2),('pair',3)))
_OsOneIpMngCfgListType_Type.__name__=_C
_OsOneIpMngCfgListType_Object=MibTableColumn
osOneIpMngCfgListType=_OsOneIpMngCfgListType_Object((1,3,6,1,4,1,6926,2,43,1,1,3,1,3),_OsOneIpMngCfgListType_Type())
osOneIpMngCfgListType.setMaxAccess(_F)
if mibBuilder.loadTexts:osOneIpMngCfgListType.setStatus(_A)
class _OsOneIpMngCfgStdFirstPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OsOneIpMngCfgStdFirstPort_Type.__name__=_D
_OsOneIpMngCfgStdFirstPort_Object=MibTableColumn
osOneIpMngCfgStdFirstPort=_OsOneIpMngCfgStdFirstPort_Object((1,3,6,1,4,1,6926,2,43,1,1,3,1,4),_OsOneIpMngCfgStdFirstPort_Type())
osOneIpMngCfgStdFirstPort.setMaxAccess(_F)
if mibBuilder.loadTexts:osOneIpMngCfgStdFirstPort.setStatus(_A)
class _OsOneIpMngCfgStdLastPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OsOneIpMngCfgStdLastPort_Type.__name__=_D
_OsOneIpMngCfgStdLastPort_Object=MibTableColumn
osOneIpMngCfgStdLastPort=_OsOneIpMngCfgStdLastPort_Object((1,3,6,1,4,1,6926,2,43,1,1,3,1,5),_OsOneIpMngCfgStdLastPort_Type())
osOneIpMngCfgStdLastPort.setMaxAccess(_F)
if mibBuilder.loadTexts:osOneIpMngCfgStdLastPort.setStatus(_A)
class _OsOneIpMngCfgAltFirstPort_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OsOneIpMngCfgAltFirstPort_Type.__name__=_D
_OsOneIpMngCfgAltFirstPort_Object=MibTableColumn
osOneIpMngCfgAltFirstPort=_OsOneIpMngCfgAltFirstPort_Object((1,3,6,1,4,1,6926,2,43,1,1,3,1,6),_OsOneIpMngCfgAltFirstPort_Type())
osOneIpMngCfgAltFirstPort.setMaxAccess(_F)
if mibBuilder.loadTexts:osOneIpMngCfgAltFirstPort.setStatus(_A)
class _OsOneIpMngCfgAltLastPort_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OsOneIpMngCfgAltLastPort_Type.__name__=_D
_OsOneIpMngCfgAltLastPort_Object=MibTableColumn
osOneIpMngCfgAltLastPort=_OsOneIpMngCfgAltLastPort_Object((1,3,6,1,4,1,6926,2,43,1,1,3,1,7),_OsOneIpMngCfgAltLastPort_Type())
osOneIpMngCfgAltLastPort.setMaxAccess(_F)
if mibBuilder.loadTexts:osOneIpMngCfgAltLastPort.setStatus(_A)
class _OsOneIpMngCfgOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('defaultOriginal',1),('defaultModified',2),('hotDefault',3)))
_OsOneIpMngCfgOperStatus_Type.__name__=_C
_OsOneIpMngCfgOperStatus_Object=MibTableColumn
osOneIpMngCfgOperStatus=_OsOneIpMngCfgOperStatus_Object((1,3,6,1,4,1,6926,2,43,1,1,3,1,98),_OsOneIpMngCfgOperStatus_Type())
osOneIpMngCfgOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:osOneIpMngCfgOperStatus.setStatus(_A)
class _OsOneIpMngCfgAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_OsOneIpMngCfgAdminStatus_Type.__name__=_C
_OsOneIpMngCfgAdminStatus_Object=MibTableColumn
osOneIpMngCfgAdminStatus=_OsOneIpMngCfgAdminStatus_Object((1,3,6,1,4,1,6926,2,43,1,1,3,1,99),_OsOneIpMngCfgAdminStatus_Type())
osOneIpMngCfgAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:osOneIpMngCfgAdminStatus.setStatus(_A)
_OsOneIpMngNatGlb_ObjectIdentity=ObjectIdentity
osOneIpMngNatGlb=_OsOneIpMngNatGlb_ObjectIdentity((1,3,6,1,4,1,6926,2,43,1,2))
class _OsOneIpManagFeatOpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_OsOneIpManagFeatOpStatus_Type.__name__=_C
_OsOneIpManagFeatOpStatus_Object=MibScalar
osOneIpManagFeatOpStatus=_OsOneIpManagFeatOpStatus_Object((1,3,6,1,4,1,6926,2,43,1,2,1),_OsOneIpManagFeatOpStatus_Type())
osOneIpManagFeatOpStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:osOneIpManagFeatOpStatus.setStatus(_A)
_OsOneIpMngNatConformance_ObjectIdentity=ObjectIdentity
osOneIpMngNatConformance=_OsOneIpMngNatConformance_ObjectIdentity((1,3,6,1,4,1,6926,2,43,101))
_OsOneIpMngNatMIBCompliances_ObjectIdentity=ObjectIdentity
osOneIpMngNatMIBCompliances=_OsOneIpMngNatMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,43,101,1))
_OsOneIpMngNatMIBGroups_ObjectIdentity=ObjectIdentity
osOneIpMngNatMIBGroups=_OsOneIpMngNatMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,43,101,2))
osOneIpMngNatMandatoryGroup=ObjectGroup((1,3,6,1,4,1,6926,2,43,101,2,1))
osOneIpMngNatMandatoryGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:osOneIpMngNatMandatoryGroup.setStatus(_A)
osOneIpMngNatMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,43,101,1,1))
osOneIpMngNatMIBCompliance.setObjects((_B,_a))
if mibBuilder.loadTexts:osOneIpMngNatMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'osOneIpMng':osOneIpMng,'osOneIpMngNat':osOneIpMngNat,'osOneIpMngNatGen':osOneIpMngNatGen,'osOneIpMngDefaultTable':osOneIpMngDefaultTable,'osOneIpMngDefaultEntry':osOneIpMngDefaultEntry,_G:osOneIpMngDefName,_L:osOneIpMngDefTransport,_M:osOneIpMngDefListType,_N:osOneIpMngDefStdFirstPort,_O:osOneIpMngDefStdLastPort,_P:osOneIpMngDefAltFirstPort,_Q:osOneIpMngDefAltLastPort,_R:osOneIpMngDefOperStatus,'osOneIpMngProtoTable':osOneIpMngProtoTable,'osOneIpMngProtoEntry':osOneIpMngProtoEntry,_J:osOneIpMngCfgName,_S:osOneIpMngCfgTransport,_T:osOneIpMngCfgListType,_U:osOneIpMngCfgStdFirstPort,_V:osOneIpMngCfgStdLastPort,_W:osOneIpMngCfgAltFirstPort,_X:osOneIpMngCfgAltLastPort,_Y:osOneIpMngCfgOperStatus,_Z:osOneIpMngCfgAdminStatus,'osOneIpMngNatGlb':osOneIpMngNatGlb,_K:osOneIpManagFeatOpStatus,'osOneIpMngNatConformance':osOneIpMngNatConformance,'osOneIpMngNatMIBCompliances':osOneIpMngNatMIBCompliances,'osOneIpMngNatMIBCompliance':osOneIpMngNatMIBCompliance,'osOneIpMngNatMIBGroups':osOneIpMngNatMIBGroups,_a:osOneIpMngNatMandatoryGroup})