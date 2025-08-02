_k='etsysVsbChassisGroup2'
_j='etsysVsbSystemGroup2'
_i='etsysVsbChassisGroup'
_h='etsysVsbSystemGroup'
_g='etsysVsbChassisLfrOperPriority'
_f='etsysVsbSystemLinkFailureResponse'
_e='etsysVsbPortOperStatus'
_d='etsysVsbPortAdminStatus'
_c='etsysVsbChassisIndex'
_b='disabled'
_a='enabled'
_Z='Unsigned32'
_Y='ifIndex'
_X='IF-MIB'
_W='etsysVsbPortGroup'
_V='etsysVsbChassisSecretEntered'
_U='etsysVsbChassisSharedSecret'
_T='etsysVsbChassisLastBondTime'
_S='etsysVsbChassisStatus'
_R='etsysVsbChassisSystemSlotList'
_Q='etsysVsbChassisLocalSlotList'
_P='etsysVsbChassisFirstSlotNumber'
_O='etsysVsbChassisSerialNum'
_N='etsysVsbChassisSystemId'
_M='deprecated'
_L='etsysVsbOperationalMacAddress'
_K='etsysVsbAdministrativeMacAddress'
_J='etsysVsbSystemMaxSlotNumber'
_I='etsysVsbSystemMaxChassis'
_H='etsysVsbSystemEnable'
_G='down'
_F='SnmpAdminString'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='current'
_A='ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ifIndex,=mibBuilder.importSymbols(_X,_Y)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Z,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeStamp','TruthValue')
etsysVirtualSwitchBondingMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,83))
if mibBuilder.loadTexts:etsysVirtualSwitchBondingMIB.setRevisions(('2012-03-13 19:14','2012-02-07 15:53','2011-12-13 20:31'))
class VsbId(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,8))
class VsbChassisStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),(_G,2),('incomplete',3),('inactive',4)))
class VsbSlotList(TextualConvention,OctetString):status=_B
_EtsysVsbObjects_ObjectIdentity=ObjectIdentity
etsysVsbObjects=_EtsysVsbObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,83,1))
_EtsysVsbSystem_ObjectIdentity=ObjectIdentity
etsysVsbSystem=_EtsysVsbSystem_ObjectIdentity((1,3,6,1,4,1,5624,1,2,83,1,1))
class _EtsysVsbSystemEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),(_b,2)))
_EtsysVsbSystemEnable_Type.__name__=_E
_EtsysVsbSystemEnable_Object=MibScalar
etsysVsbSystemEnable=_EtsysVsbSystemEnable_Object((1,3,6,1,4,1,5624,1,2,83,1,1,1),_EtsysVsbSystemEnable_Type())
etsysVsbSystemEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysVsbSystemEnable.setStatus(_B)
_EtsysVsbSystemMaxChassis_Type=Unsigned32
_EtsysVsbSystemMaxChassis_Object=MibScalar
etsysVsbSystemMaxChassis=_EtsysVsbSystemMaxChassis_Object((1,3,6,1,4,1,5624,1,2,83,1,1,2),_EtsysVsbSystemMaxChassis_Type())
etsysVsbSystemMaxChassis.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysVsbSystemMaxChassis.setStatus(_B)
_EtsysVsbSystemMaxSlotNumber_Type=Unsigned32
_EtsysVsbSystemMaxSlotNumber_Object=MibScalar
etsysVsbSystemMaxSlotNumber=_EtsysVsbSystemMaxSlotNumber_Object((1,3,6,1,4,1,5624,1,2,83,1,1,3),_EtsysVsbSystemMaxSlotNumber_Type())
etsysVsbSystemMaxSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysVsbSystemMaxSlotNumber.setStatus(_B)
_EtsysVsbAdministrativeMacAddress_Type=MacAddress
_EtsysVsbAdministrativeMacAddress_Object=MibScalar
etsysVsbAdministrativeMacAddress=_EtsysVsbAdministrativeMacAddress_Object((1,3,6,1,4,1,5624,1,2,83,1,1,4),_EtsysVsbAdministrativeMacAddress_Type())
etsysVsbAdministrativeMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysVsbAdministrativeMacAddress.setStatus(_B)
_EtsysVsbOperationalMacAddress_Type=MacAddress
_EtsysVsbOperationalMacAddress_Object=MibScalar
etsysVsbOperationalMacAddress=_EtsysVsbOperationalMacAddress_Object((1,3,6,1,4,1,5624,1,2,83,1,1,5),_EtsysVsbOperationalMacAddress_Type())
etsysVsbOperationalMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysVsbOperationalMacAddress.setStatus(_B)
class _EtsysVsbSystemLinkFailureResponse_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),(_b,2)))
_EtsysVsbSystemLinkFailureResponse_Type.__name__=_E
_EtsysVsbSystemLinkFailureResponse_Object=MibScalar
etsysVsbSystemLinkFailureResponse=_EtsysVsbSystemLinkFailureResponse_Object((1,3,6,1,4,1,5624,1,2,83,1,1,6),_EtsysVsbSystemLinkFailureResponse_Type())
etsysVsbSystemLinkFailureResponse.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysVsbSystemLinkFailureResponse.setStatus(_B)
_EtsysVsbChassis_ObjectIdentity=ObjectIdentity
etsysVsbChassis=_EtsysVsbChassis_ObjectIdentity((1,3,6,1,4,1,5624,1,2,83,1,2))
_EtsysVsbChassisTable_Object=MibTable
etsysVsbChassisTable=_EtsysVsbChassisTable_Object((1,3,6,1,4,1,5624,1,2,83,1,2,1))
if mibBuilder.loadTexts:etsysVsbChassisTable.setStatus(_B)
_EtsysVsbChassisEntry_Object=MibTableRow
etsysVsbChassisEntry=_EtsysVsbChassisEntry_Object((1,3,6,1,4,1,5624,1,2,83,1,2,1,1))
etsysVsbChassisEntry.setIndexNames((0,_A,_c))
if mibBuilder.loadTexts:etsysVsbChassisEntry.setStatus(_B)
_EtsysVsbChassisIndex_Type=Unsigned32
_EtsysVsbChassisIndex_Object=MibTableColumn
etsysVsbChassisIndex=_EtsysVsbChassisIndex_Object((1,3,6,1,4,1,5624,1,2,83,1,2,1,1,1),_EtsysVsbChassisIndex_Type())
etsysVsbChassisIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:etsysVsbChassisIndex.setStatus(_B)
_EtsysVsbChassisSystemId_Type=VsbId
_EtsysVsbChassisSystemId_Object=MibTableColumn
etsysVsbChassisSystemId=_EtsysVsbChassisSystemId_Object((1,3,6,1,4,1,5624,1,2,83,1,2,1,1,2),_EtsysVsbChassisSystemId_Type())
etsysVsbChassisSystemId.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysVsbChassisSystemId.setStatus(_B)
class _EtsysVsbChassisSerialNum_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EtsysVsbChassisSerialNum_Type.__name__=_F
_EtsysVsbChassisSerialNum_Object=MibTableColumn
etsysVsbChassisSerialNum=_EtsysVsbChassisSerialNum_Object((1,3,6,1,4,1,5624,1,2,83,1,2,1,1,3),_EtsysVsbChassisSerialNum_Type())
etsysVsbChassisSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysVsbChassisSerialNum.setStatus(_B)
class _EtsysVsbChassisFirstSlotNumber_Type(Unsigned32):defaultValue=0
_EtsysVsbChassisFirstSlotNumber_Type.__name__=_Z
_EtsysVsbChassisFirstSlotNumber_Object=MibTableColumn
etsysVsbChassisFirstSlotNumber=_EtsysVsbChassisFirstSlotNumber_Object((1,3,6,1,4,1,5624,1,2,83,1,2,1,1,4),_EtsysVsbChassisFirstSlotNumber_Type())
etsysVsbChassisFirstSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysVsbChassisFirstSlotNumber.setStatus(_B)
_EtsysVsbChassisLocalSlotList_Type=VsbSlotList
_EtsysVsbChassisLocalSlotList_Object=MibTableColumn
etsysVsbChassisLocalSlotList=_EtsysVsbChassisLocalSlotList_Object((1,3,6,1,4,1,5624,1,2,83,1,2,1,1,5),_EtsysVsbChassisLocalSlotList_Type())
etsysVsbChassisLocalSlotList.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysVsbChassisLocalSlotList.setStatus(_B)
_EtsysVsbChassisSystemSlotList_Type=VsbSlotList
_EtsysVsbChassisSystemSlotList_Object=MibTableColumn
etsysVsbChassisSystemSlotList=_EtsysVsbChassisSystemSlotList_Object((1,3,6,1,4,1,5624,1,2,83,1,2,1,1,6),_EtsysVsbChassisSystemSlotList_Type())
etsysVsbChassisSystemSlotList.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysVsbChassisSystemSlotList.setStatus(_B)
_EtsysVsbChassisStatus_Type=VsbChassisStatus
_EtsysVsbChassisStatus_Object=MibTableColumn
etsysVsbChassisStatus=_EtsysVsbChassisStatus_Object((1,3,6,1,4,1,5624,1,2,83,1,2,1,1,7),_EtsysVsbChassisStatus_Type())
etsysVsbChassisStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysVsbChassisStatus.setStatus(_B)
_EtsysVsbChassisLastBondTime_Type=TimeStamp
_EtsysVsbChassisLastBondTime_Object=MibTableColumn
etsysVsbChassisLastBondTime=_EtsysVsbChassisLastBondTime_Object((1,3,6,1,4,1,5624,1,2,83,1,2,1,1,8),_EtsysVsbChassisLastBondTime_Type())
etsysVsbChassisLastBondTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysVsbChassisLastBondTime.setStatus(_B)
class _EtsysVsbChassisSharedSecret_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EtsysVsbChassisSharedSecret_Type.__name__=_F
_EtsysVsbChassisSharedSecret_Object=MibTableColumn
etsysVsbChassisSharedSecret=_EtsysVsbChassisSharedSecret_Object((1,3,6,1,4,1,5624,1,2,83,1,2,1,1,9),_EtsysVsbChassisSharedSecret_Type())
etsysVsbChassisSharedSecret.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysVsbChassisSharedSecret.setStatus(_B)
_EtsysVsbChassisSecretEntered_Type=TruthValue
_EtsysVsbChassisSecretEntered_Object=MibTableColumn
etsysVsbChassisSecretEntered=_EtsysVsbChassisSecretEntered_Object((1,3,6,1,4,1,5624,1,2,83,1,2,1,1,10),_EtsysVsbChassisSecretEntered_Type())
etsysVsbChassisSecretEntered.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysVsbChassisSecretEntered.setStatus(_B)
_EtsysVsbChassisLfrOperPriority_Type=Unsigned32
_EtsysVsbChassisLfrOperPriority_Object=MibTableColumn
etsysVsbChassisLfrOperPriority=_EtsysVsbChassisLfrOperPriority_Object((1,3,6,1,4,1,5624,1,2,83,1,2,1,1,11),_EtsysVsbChassisLfrOperPriority_Type())
etsysVsbChassisLfrOperPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysVsbChassisLfrOperPriority.setStatus(_B)
_EtsysVsbPort_ObjectIdentity=ObjectIdentity
etsysVsbPort=_EtsysVsbPort_ObjectIdentity((1,3,6,1,4,1,5624,1,2,83,1,3))
_EtsysVsbPortTable_Object=MibTable
etsysVsbPortTable=_EtsysVsbPortTable_Object((1,3,6,1,4,1,5624,1,2,83,1,3,1))
if mibBuilder.loadTexts:etsysVsbPortTable.setStatus(_B)
_EtsysVsbPortEntry_Object=MibTableRow
etsysVsbPortEntry=_EtsysVsbPortEntry_Object((1,3,6,1,4,1,5624,1,2,83,1,3,1,1))
etsysVsbPortEntry.setIndexNames((0,_X,_Y))
if mibBuilder.loadTexts:etsysVsbPortEntry.setStatus(_B)
class _EtsysVsbPortAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_G,2)))
_EtsysVsbPortAdminStatus_Type.__name__=_E
_EtsysVsbPortAdminStatus_Object=MibTableColumn
etsysVsbPortAdminStatus=_EtsysVsbPortAdminStatus_Object((1,3,6,1,4,1,5624,1,2,83,1,3,1,1,1),_EtsysVsbPortAdminStatus_Type())
etsysVsbPortAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysVsbPortAdminStatus.setStatus(_B)
class _EtsysVsbPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('up',1),(_G,2),('highLatency',3),('probeLoop',4),('probeTimeout',5),('portInstability',6)))
_EtsysVsbPortOperStatus_Type.__name__=_E
_EtsysVsbPortOperStatus_Object=MibTableColumn
etsysVsbPortOperStatus=_EtsysVsbPortOperStatus_Object((1,3,6,1,4,1,5624,1,2,83,1,3,1,1,2),_EtsysVsbPortOperStatus_Type())
etsysVsbPortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysVsbPortOperStatus.setStatus(_B)
_EtsysVsbConformance_ObjectIdentity=ObjectIdentity
etsysVsbConformance=_EtsysVsbConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,83,2))
_EtsysVsbGroups_ObjectIdentity=ObjectIdentity
etsysVsbGroups=_EtsysVsbGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,83,2,1))
_EtsysVsbCompliances_ObjectIdentity=ObjectIdentity
etsysVsbCompliances=_EtsysVsbCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,83,2,2))
etsysVsbSystemGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,83,2,1,1))
etsysVsbSystemGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:etsysVsbSystemGroup.setStatus(_M)
etsysVsbChassisGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,83,2,1,2))
etsysVsbChassisGroup.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:etsysVsbChassisGroup.setStatus(_M)
etsysVsbPortGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,83,2,1,3))
etsysVsbPortGroup.setObjects(*((_A,_d),(_A,_e)))
if mibBuilder.loadTexts:etsysVsbPortGroup.setStatus(_B)
etsysVsbSystemGroup2=ObjectGroup((1,3,6,1,4,1,5624,1,2,83,2,1,4))
etsysVsbSystemGroup2.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_f)))
if mibBuilder.loadTexts:etsysVsbSystemGroup2.setStatus(_B)
etsysVsbChassisGroup2=ObjectGroup((1,3,6,1,4,1,5624,1,2,83,2,1,5))
etsysVsbChassisGroup2.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_g)))
if mibBuilder.loadTexts:etsysVsbChassisGroup2.setStatus(_B)
etsysVsbCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,83,2,2,1))
etsysVsbCompliance.setObjects(*((_A,_h),(_A,_i),(_A,_W)))
if mibBuilder.loadTexts:etsysVsbCompliance.setStatus(_M)
etsysVsbCompliance2=ModuleCompliance((1,3,6,1,4,1,5624,1,2,83,2,2,2))
etsysVsbCompliance2.setObjects(*((_A,_j),(_A,_k),(_A,_W)))
if mibBuilder.loadTexts:etsysVsbCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'VsbId':VsbId,'VsbChassisStatus':VsbChassisStatus,'VsbSlotList':VsbSlotList,'etsysVirtualSwitchBondingMIB':etsysVirtualSwitchBondingMIB,'etsysVsbObjects':etsysVsbObjects,'etsysVsbSystem':etsysVsbSystem,_H:etsysVsbSystemEnable,_I:etsysVsbSystemMaxChassis,_J:etsysVsbSystemMaxSlotNumber,_K:etsysVsbAdministrativeMacAddress,_L:etsysVsbOperationalMacAddress,_f:etsysVsbSystemLinkFailureResponse,'etsysVsbChassis':etsysVsbChassis,'etsysVsbChassisTable':etsysVsbChassisTable,'etsysVsbChassisEntry':etsysVsbChassisEntry,_c:etsysVsbChassisIndex,_N:etsysVsbChassisSystemId,_O:etsysVsbChassisSerialNum,_P:etsysVsbChassisFirstSlotNumber,_Q:etsysVsbChassisLocalSlotList,_R:etsysVsbChassisSystemSlotList,_S:etsysVsbChassisStatus,_T:etsysVsbChassisLastBondTime,_U:etsysVsbChassisSharedSecret,_V:etsysVsbChassisSecretEntered,_g:etsysVsbChassisLfrOperPriority,'etsysVsbPort':etsysVsbPort,'etsysVsbPortTable':etsysVsbPortTable,'etsysVsbPortEntry':etsysVsbPortEntry,_d:etsysVsbPortAdminStatus,_e:etsysVsbPortOperStatus,'etsysVsbConformance':etsysVsbConformance,'etsysVsbGroups':etsysVsbGroups,_h:etsysVsbSystemGroup,_i:etsysVsbChassisGroup,_W:etsysVsbPortGroup,_j:etsysVsbSystemGroup2,_k:etsysVsbChassisGroup2,'etsysVsbCompliances':etsysVsbCompliances,'etsysVsbCompliance':etsysVsbCompliance,'etsysVsbCompliance2':etsysVsbCompliance2})