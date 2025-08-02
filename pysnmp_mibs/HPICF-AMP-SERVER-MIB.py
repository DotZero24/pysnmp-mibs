_Z='hpicfArubaVPNConfigGroup1'
_Y='hpicfArubaVPNBkpIP'
_X='hpicfArubaVPNBkpIPType'
_W='hpicfArubaVPNGateway'
_V='hpicfAMPServerRetryInterval'
_U='hpicfAMPServerConfigStatus'
_T='hpicfAMPServerSecret'
_S='hpicfAMPServerFolder'
_R='hpicfAMPServerGroup'
_Q='hpicfAMPServerIPType'
_P='hpicfAMPServerIP'
_O='hpicfArubaVPNIndex'
_N='Integer32'
_M='hpicfDefaultGatewayGroup'
_L='hpicfArubaVPNConfigGroup'
_K='deprecated'
_J='hpicfArubaVPNTtl'
_I='hpicfArubaVPNTos'
_H='hpicfArubaVPNIP'
_G='hpicfArubaVPNIPType'
_F='hpicfArubaVPNRowStatus'
_E='hpicfAMPServerConfigGroup'
_D='OctetString'
_C='read-write'
_B='current'
_A='HPICF-AMP-SERVER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_N,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
hpicfAMPServerMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,125))
if mibBuilder.loadTexts:hpicfAMPServerMIB.setRevisions(('2020-01-17 00:00','2017-03-07 00:00','2017-01-04 00:00','2016-12-16 00:00','2016-09-15 00:00','2016-04-19 00:00','2016-03-03 00:00','2015-12-14 00:00'))
class HpicfArubaVPNType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('amp',2),('any',3)))
_HpicfAMPServerObjects_ObjectIdentity=ObjectIdentity
hpicfAMPServerObjects=_HpicfAMPServerObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,125,1))
_HpicfAMPServerIPType_Type=InetAddressType
_HpicfAMPServerIPType_Object=MibScalar
hpicfAMPServerIPType=_HpicfAMPServerIPType_Object((1,3,6,1,4,1,11,2,14,11,5,1,125,1,1),_HpicfAMPServerIPType_Type())
hpicfAMPServerIPType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfAMPServerIPType.setStatus(_B)
_HpicfAMPServerIP_Type=InetAddress
_HpicfAMPServerIP_Object=MibScalar
hpicfAMPServerIP=_HpicfAMPServerIP_Object((1,3,6,1,4,1,11,2,14,11,5,1,125,1,2),_HpicfAMPServerIP_Type())
hpicfAMPServerIP.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfAMPServerIP.setStatus(_B)
class _HpicfAMPServerGroup_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpicfAMPServerGroup_Type.__name__=_D
_HpicfAMPServerGroup_Object=MibScalar
hpicfAMPServerGroup=_HpicfAMPServerGroup_Object((1,3,6,1,4,1,11,2,14,11,5,1,125,1,3),_HpicfAMPServerGroup_Type())
hpicfAMPServerGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfAMPServerGroup.setStatus(_B)
class _HpicfAMPServerFolder_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HpicfAMPServerFolder_Type.__name__=_D
_HpicfAMPServerFolder_Object=MibScalar
hpicfAMPServerFolder=_HpicfAMPServerFolder_Object((1,3,6,1,4,1,11,2,14,11,5,1,125,1,4),_HpicfAMPServerFolder_Type())
hpicfAMPServerFolder.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfAMPServerFolder.setStatus(_B)
class _HpicfAMPServerSecret_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpicfAMPServerSecret_Type.__name__=_D
_HpicfAMPServerSecret_Object=MibScalar
hpicfAMPServerSecret=_HpicfAMPServerSecret_Object((1,3,6,1,4,1,11,2,14,11,5,1,125,1,5),_HpicfAMPServerSecret_Type())
hpicfAMPServerSecret.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfAMPServerSecret.setStatus(_B)
class _HpicfAMPServerConfigStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('configured',1),('notConfigured',2)))
_HpicfAMPServerConfigStatus_Type.__name__=_N
_HpicfAMPServerConfigStatus_Object=MibScalar
hpicfAMPServerConfigStatus=_HpicfAMPServerConfigStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,125,1,6),_HpicfAMPServerConfigStatus_Type())
hpicfAMPServerConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfAMPServerConfigStatus.setStatus(_B)
_HpicfAMPServerRetryInterval_Type=Integer32
_HpicfAMPServerRetryInterval_Object=MibScalar
hpicfAMPServerRetryInterval=_HpicfAMPServerRetryInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,125,1,7),_HpicfAMPServerRetryInterval_Type())
hpicfAMPServerRetryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfAMPServerRetryInterval.setStatus(_B)
if mibBuilder.loadTexts:hpicfAMPServerRetryInterval.setUnits('Seconds')
_HpicfAMPServerConformance_ObjectIdentity=ObjectIdentity
hpicfAMPServerConformance=_HpicfAMPServerConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,125,2))
_HpicfAMPServerMIBCompliances_ObjectIdentity=ObjectIdentity
hpicfAMPServerMIBCompliances=_HpicfAMPServerMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,125,2,1))
_HpicfAMPServerMIBGroups_ObjectIdentity=ObjectIdentity
hpicfAMPServerMIBGroups=_HpicfAMPServerMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,125,2,2))
_HpicfArubaVPNObjects_ObjectIdentity=ObjectIdentity
hpicfArubaVPNObjects=_HpicfArubaVPNObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,125,3))
_HpicfArubaVPNTable_Object=MibTable
hpicfArubaVPNTable=_HpicfArubaVPNTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,125,3,1))
if mibBuilder.loadTexts:hpicfArubaVPNTable.setStatus(_B)
_HpicfArubaVPNEntry_Object=MibTableRow
hpicfArubaVPNEntry=_HpicfArubaVPNEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,125,3,1,1))
hpicfArubaVPNEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:hpicfArubaVPNEntry.setStatus(_B)
_HpicfArubaVPNIndex_Type=HpicfArubaVPNType
_HpicfArubaVPNIndex_Object=MibTableColumn
hpicfArubaVPNIndex=_HpicfArubaVPNIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,125,3,1,1,1),_HpicfArubaVPNIndex_Type())
hpicfArubaVPNIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpicfArubaVPNIndex.setStatus(_B)
_HpicfArubaVPNRowStatus_Type=RowStatus
_HpicfArubaVPNRowStatus_Object=MibTableColumn
hpicfArubaVPNRowStatus=_HpicfArubaVPNRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,125,3,1,1,2),_HpicfArubaVPNRowStatus_Type())
hpicfArubaVPNRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:hpicfArubaVPNRowStatus.setStatus(_B)
_HpicfArubaVPNIPType_Type=InetAddressType
_HpicfArubaVPNIPType_Object=MibTableColumn
hpicfArubaVPNIPType=_HpicfArubaVPNIPType_Object((1,3,6,1,4,1,11,2,14,11,5,1,125,3,1,1,3),_HpicfArubaVPNIPType_Type())
hpicfArubaVPNIPType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfArubaVPNIPType.setStatus(_B)
_HpicfArubaVPNIP_Type=InetAddress
_HpicfArubaVPNIP_Object=MibTableColumn
hpicfArubaVPNIP=_HpicfArubaVPNIP_Object((1,3,6,1,4,1,11,2,14,11,5,1,125,3,1,1,4),_HpicfArubaVPNIP_Type())
hpicfArubaVPNIP.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfArubaVPNIP.setStatus(_B)
_HpicfArubaVPNTos_Type=Integer32
_HpicfArubaVPNTos_Object=MibTableColumn
hpicfArubaVPNTos=_HpicfArubaVPNTos_Object((1,3,6,1,4,1,11,2,14,11,5,1,125,3,1,1,5),_HpicfArubaVPNTos_Type())
hpicfArubaVPNTos.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfArubaVPNTos.setStatus(_B)
_HpicfArubaVPNTtl_Type=Integer32
_HpicfArubaVPNTtl_Object=MibTableColumn
hpicfArubaVPNTtl=_HpicfArubaVPNTtl_Object((1,3,6,1,4,1,11,2,14,11,5,1,125,3,1,1,6),_HpicfArubaVPNTtl_Type())
hpicfArubaVPNTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfArubaVPNTtl.setStatus(_B)
_HpicfArubaVPNBkpIPType_Type=InetAddressType
_HpicfArubaVPNBkpIPType_Object=MibTableColumn
hpicfArubaVPNBkpIPType=_HpicfArubaVPNBkpIPType_Object((1,3,6,1,4,1,11,2,14,11,5,1,125,3,1,1,7),_HpicfArubaVPNBkpIPType_Type())
hpicfArubaVPNBkpIPType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfArubaVPNBkpIPType.setStatus(_B)
_HpicfArubaVPNBkpIP_Type=InetAddress
_HpicfArubaVPNBkpIP_Object=MibTableColumn
hpicfArubaVPNBkpIP=_HpicfArubaVPNBkpIP_Object((1,3,6,1,4,1,11,2,14,11,5,1,125,3,1,1,8),_HpicfArubaVPNBkpIP_Type())
hpicfArubaVPNBkpIP.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfArubaVPNBkpIP.setStatus(_B)
_HpicfArubaVPNDefaultGateway_ObjectIdentity=ObjectIdentity
hpicfArubaVPNDefaultGateway=_HpicfArubaVPNDefaultGateway_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,125,4))
_HpicfArubaVPNGateway_Type=TruthValue
_HpicfArubaVPNGateway_Object=MibScalar
hpicfArubaVPNGateway=_HpicfArubaVPNGateway_Object((1,3,6,1,4,1,11,2,14,11,5,1,125,4,1),_HpicfArubaVPNGateway_Type())
hpicfArubaVPNGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfArubaVPNGateway.setStatus(_B)
hpicfAMPServerConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,125,2,2,1))
hpicfAMPServerConfigGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:hpicfAMPServerConfigGroup.setStatus(_B)
hpicfArubaVPNConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,125,2,2,2))
hpicfArubaVPNConfigGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:hpicfArubaVPNConfigGroup.setStatus(_K)
hpicfDefaultGatewayGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,125,2,2,3))
hpicfDefaultGatewayGroup.setObjects((_A,_W))
if mibBuilder.loadTexts:hpicfDefaultGatewayGroup.setStatus(_B)
hpicfArubaVPNConfigGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,125,2,2,4))
hpicfArubaVPNConfigGroup1.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:hpicfArubaVPNConfigGroup1.setStatus(_B)
hpicfAMPServerMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,125,2,1,1))
hpicfAMPServerMIBCompliance.setObjects(*((_A,_E),(_A,_L)))
if mibBuilder.loadTexts:hpicfAMPServerMIBCompliance.setStatus(_K)
hpicfAMPServerMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,125,2,1,2))
hpicfAMPServerMIBCompliance1.setObjects(*((_A,_E),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:hpicfAMPServerMIBCompliance1.setStatus(_K)
hpicfAMPServerMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,125,2,1,3))
hpicfAMPServerMIBCompliance2.setObjects(*((_A,_E),(_A,_Z),(_A,_M)))
if mibBuilder.loadTexts:hpicfAMPServerMIBCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'HpicfArubaVPNType':HpicfArubaVPNType,'hpicfAMPServerMIB':hpicfAMPServerMIB,'hpicfAMPServerObjects':hpicfAMPServerObjects,_Q:hpicfAMPServerIPType,_P:hpicfAMPServerIP,_R:hpicfAMPServerGroup,_S:hpicfAMPServerFolder,_T:hpicfAMPServerSecret,_U:hpicfAMPServerConfigStatus,_V:hpicfAMPServerRetryInterval,'hpicfAMPServerConformance':hpicfAMPServerConformance,'hpicfAMPServerMIBCompliances':hpicfAMPServerMIBCompliances,'hpicfAMPServerMIBCompliance':hpicfAMPServerMIBCompliance,'hpicfAMPServerMIBCompliance1':hpicfAMPServerMIBCompliance1,'hpicfAMPServerMIBCompliance2':hpicfAMPServerMIBCompliance2,'hpicfAMPServerMIBGroups':hpicfAMPServerMIBGroups,_E:hpicfAMPServerConfigGroup,_L:hpicfArubaVPNConfigGroup,_M:hpicfDefaultGatewayGroup,_Z:hpicfArubaVPNConfigGroup1,'hpicfArubaVPNObjects':hpicfArubaVPNObjects,'hpicfArubaVPNTable':hpicfArubaVPNTable,'hpicfArubaVPNEntry':hpicfArubaVPNEntry,_O:hpicfArubaVPNIndex,_F:hpicfArubaVPNRowStatus,_G:hpicfArubaVPNIPType,_H:hpicfArubaVPNIP,_I:hpicfArubaVPNTos,_J:hpicfArubaVPNTtl,_X:hpicfArubaVPNBkpIPType,_Y:hpicfArubaVPNBkpIP,'hpicfArubaVPNDefaultGateway':hpicfArubaVPNDefaultGateway,_W:hpicfArubaVPNGateway})