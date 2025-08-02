_P='oaDevTrunkMandatoryGroup'
_O='oaDevTrunkGrPortLogicalNumber'
_N='oaDevTrunkGrAdminStatus'
_M='oaDevTrunkGrPortsNumber'
_L='oaDevTrunkGrPortMembers'
_K='oaDevTrunkGrDescription'
_J='oaDevTrunkGrNumber'
_I='oaDevTrunkGenSupport'
_H='oaDevTrunkGrId'
_G='DisplayString'
_F='OctetString'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='OA-DEV-TRUNKS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
oaDeviceTrunks=ModuleIdentity((1,3,6,1,4,1,629,1,50,11,1,23))
if mibBuilder.loadTexts:oaDeviceTrunks.setRevisions(('2007-12-11 00:00','2007-08-02 00:00'))
_Nbase_ObjectIdentity=ObjectIdentity
nbase=_Nbase_ObjectIdentity((1,3,6,1,4,1,629))
_NbSwitchG1_ObjectIdentity=ObjectIdentity
nbSwitchG1=_NbSwitchG1_ObjectIdentity((1,3,6,1,4,1,629,1))
_NbSwitchG1Il_ObjectIdentity=ObjectIdentity
nbSwitchG1Il=_NbSwitchG1Il_ObjectIdentity((1,3,6,1,4,1,629,1,50))
_NbDeviceConfig_ObjectIdentity=ObjectIdentity
nbDeviceConfig=_NbDeviceConfig_ObjectIdentity((1,3,6,1,4,1,629,1,50,11))
_NbDevGen_ObjectIdentity=ObjectIdentity
nbDevGen=_NbDevGen_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1))
_OaDevTrunkGen_ObjectIdentity=ObjectIdentity
oaDevTrunkGen=_OaDevTrunkGen_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,23,1))
class _OaDevTrunkGenSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSupported',1),('supported',2)))
_OaDevTrunkGenSupport_Type.__name__=_C
_OaDevTrunkGenSupport_Object=MibScalar
oaDevTrunkGenSupport=_OaDevTrunkGenSupport_Object((1,3,6,1,4,1,629,1,50,11,1,23,1,1),_OaDevTrunkGenSupport_Type())
oaDevTrunkGenSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevTrunkGenSupport.setStatus(_A)
_OaDevTrunks_ObjectIdentity=ObjectIdentity
oaDevTrunks=_OaDevTrunks_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,23,2))
_OaDevTrunkGrNumber_Type=Integer32
_OaDevTrunkGrNumber_Object=MibScalar
oaDevTrunkGrNumber=_OaDevTrunkGrNumber_Object((1,3,6,1,4,1,629,1,50,11,1,23,2,1),_OaDevTrunkGrNumber_Type())
oaDevTrunkGrNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevTrunkGrNumber.setStatus(_A)
_OaDevTrunkGrTable_Object=MibTable
oaDevTrunkGrTable=_OaDevTrunkGrTable_Object((1,3,6,1,4,1,629,1,50,11,1,23,2,5))
if mibBuilder.loadTexts:oaDevTrunkGrTable.setStatus(_A)
_OaDevTrunkGrEntry_Object=MibTableRow
oaDevTrunkGrEntry=_OaDevTrunkGrEntry_Object((1,3,6,1,4,1,629,1,50,11,1,23,2,5,1))
oaDevTrunkGrEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:oaDevTrunkGrEntry.setStatus(_A)
class _OaDevTrunkGrId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OaDevTrunkGrId_Type.__name__=_C
_OaDevTrunkGrId_Object=MibTableColumn
oaDevTrunkGrId=_OaDevTrunkGrId_Object((1,3,6,1,4,1,629,1,50,11,1,23,2,5,1,1),_OaDevTrunkGrId_Type())
oaDevTrunkGrId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:oaDevTrunkGrId.setStatus(_A)
class _OaDevTrunkGrDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OaDevTrunkGrDescription_Type.__name__=_G
_OaDevTrunkGrDescription_Object=MibTableColumn
oaDevTrunkGrDescription=_OaDevTrunkGrDescription_Object((1,3,6,1,4,1,629,1,50,11,1,23,2,5,1,2),_OaDevTrunkGrDescription_Type())
oaDevTrunkGrDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:oaDevTrunkGrDescription.setStatus(_A)
class _OaDevTrunkGrPortMembers_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OaDevTrunkGrPortMembers_Type.__name__=_F
_OaDevTrunkGrPortMembers_Object=MibTableColumn
oaDevTrunkGrPortMembers=_OaDevTrunkGrPortMembers_Object((1,3,6,1,4,1,629,1,50,11,1,23,2,5,1,3),_OaDevTrunkGrPortMembers_Type())
oaDevTrunkGrPortMembers.setMaxAccess(_E)
if mibBuilder.loadTexts:oaDevTrunkGrPortMembers.setStatus(_A)
_OaDevTrunkGrPortsNumber_Type=Integer32
_OaDevTrunkGrPortsNumber_Object=MibTableColumn
oaDevTrunkGrPortsNumber=_OaDevTrunkGrPortsNumber_Object((1,3,6,1,4,1,629,1,50,11,1,23,2,5,1,4),_OaDevTrunkGrPortsNumber_Type())
oaDevTrunkGrPortsNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevTrunkGrPortsNumber.setStatus(_A)
class _OaDevTrunkGrAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('validId',1),('invalid',2),('validNoId',3)))
_OaDevTrunkGrAdminStatus_Type.__name__=_C
_OaDevTrunkGrAdminStatus_Object=MibTableColumn
oaDevTrunkGrAdminStatus=_OaDevTrunkGrAdminStatus_Object((1,3,6,1,4,1,629,1,50,11,1,23,2,5,1,5),_OaDevTrunkGrAdminStatus_Type())
oaDevTrunkGrAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:oaDevTrunkGrAdminStatus.setStatus(_A)
_OaDevTrunkGrPortLogicalNumber_Type=Integer32
_OaDevTrunkGrPortLogicalNumber_Object=MibTableColumn
oaDevTrunkGrPortLogicalNumber=_OaDevTrunkGrPortLogicalNumber_Object((1,3,6,1,4,1,629,1,50,11,1,23,2,5,1,6),_OaDevTrunkGrPortLogicalNumber_Type())
oaDevTrunkGrPortLogicalNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevTrunkGrPortLogicalNumber.setStatus(_A)
_OaDevTrunkConformance_ObjectIdentity=ObjectIdentity
oaDevTrunkConformance=_OaDevTrunkConformance_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,23,101))
_OaDevTrunkMIBCompliances_ObjectIdentity=ObjectIdentity
oaDevTrunkMIBCompliances=_OaDevTrunkMIBCompliances_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,23,101,1))
_OaDevTrunkMIBGroups_ObjectIdentity=ObjectIdentity
oaDevTrunkMIBGroups=_OaDevTrunkMIBGroups_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,23,101,2))
oaDevTrunkMandatoryGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,11,1,23,101,2,1))
oaDevTrunkMandatoryGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:oaDevTrunkMandatoryGroup.setStatus(_A)
oaDevTrunkMIBCompliance=ModuleCompliance((1,3,6,1,4,1,629,1,50,11,1,23,101,1,1))
oaDevTrunkMIBCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:oaDevTrunkMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'nbase':nbase,'nbSwitchG1':nbSwitchG1,'nbSwitchG1Il':nbSwitchG1Il,'nbDeviceConfig':nbDeviceConfig,'nbDevGen':nbDevGen,'oaDeviceTrunks':oaDeviceTrunks,'oaDevTrunkGen':oaDevTrunkGen,_I:oaDevTrunkGenSupport,'oaDevTrunks':oaDevTrunks,_J:oaDevTrunkGrNumber,'oaDevTrunkGrTable':oaDevTrunkGrTable,'oaDevTrunkGrEntry':oaDevTrunkGrEntry,_H:oaDevTrunkGrId,_K:oaDevTrunkGrDescription,_L:oaDevTrunkGrPortMembers,_M:oaDevTrunkGrPortsNumber,_N:oaDevTrunkGrAdminStatus,_O:oaDevTrunkGrPortLogicalNumber,'oaDevTrunkConformance':oaDevTrunkConformance,'oaDevTrunkMIBCompliances':oaDevTrunkMIBCompliances,'oaDevTrunkMIBCompliance':oaDevTrunkMIBCompliance,'oaDevTrunkMIBGroups':oaDevTrunkMIBGroups,_P:oaDevTrunkMandatoryGroup})