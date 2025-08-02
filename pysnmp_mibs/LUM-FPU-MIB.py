_N='fpuApplicationGroupV1'
_M='fpuGeneralGroupV1'
_L='fpuApplicationWavelengthBand'
_K='fpuApplicationName'
_J='fpuGeneralFpuApplicationStateLastChangeTime'
_I='fpuGeneralFpuApplicationConfigLastChangeTime'
_H='fpuGeneralFpuApplicationTableSize'
_G='fpuGeneralStateLastChangeTime'
_F='fpuGeneralConfigLastChangeTime'
_E='FpuWavelengthBand'
_D='fpuApplicationIndex'
_C='read-only'
_B='LUM-FPU-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumFpuMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumFpuMIB','lumModules')
MgmtNameString,=mibBuilder.importSymbols('LUM-TC','MgmtNameString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
lumFpuMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,66))
if mibBuilder.loadTexts:lumFpuMIBModule.setRevisions(('2017-06-15 00:00','2015-11-30 00:00'))
class FpuWavelengthBand(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1310,1550,2147483647)));namedValues=NamedValues(*(('cwdm1310',1310),('dwdm1550',1550),('notApplicable',2147483647)))
_LumFpuConfs_ObjectIdentity=ObjectIdentity
lumFpuConfs=_LumFpuConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,66,1))
_LumFpuGroups_ObjectIdentity=ObjectIdentity
lumFpuGroups=_LumFpuGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,66,1,1))
_LumFpuCompl_ObjectIdentity=ObjectIdentity
lumFpuCompl=_LumFpuCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,66,1,2))
_LumFpuMIBObjects_ObjectIdentity=ObjectIdentity
lumFpuMIBObjects=_LumFpuMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,66,2))
_FpuGeneral_ObjectIdentity=ObjectIdentity
fpuGeneral=_FpuGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,66,2,1))
_FpuGeneralConfigLastChangeTime_Type=DateAndTime
_FpuGeneralConfigLastChangeTime_Object=MibScalar
fpuGeneralConfigLastChangeTime=_FpuGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,66,2,1,1),_FpuGeneralConfigLastChangeTime_Type())
fpuGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fpuGeneralConfigLastChangeTime.setStatus(_A)
_FpuGeneralStateLastChangeTime_Type=DateAndTime
_FpuGeneralStateLastChangeTime_Object=MibScalar
fpuGeneralStateLastChangeTime=_FpuGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,66,2,1,2),_FpuGeneralStateLastChangeTime_Type())
fpuGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fpuGeneralStateLastChangeTime.setStatus(_A)
_FpuGeneralFpuApplicationTableSize_Type=Unsigned32
_FpuGeneralFpuApplicationTableSize_Object=MibScalar
fpuGeneralFpuApplicationTableSize=_FpuGeneralFpuApplicationTableSize_Object((1,3,6,1,4,1,8708,2,66,2,1,3),_FpuGeneralFpuApplicationTableSize_Type())
fpuGeneralFpuApplicationTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fpuGeneralFpuApplicationTableSize.setStatus(_A)
_FpuGeneralFpuApplicationConfigLastChangeTime_Type=DateAndTime
_FpuGeneralFpuApplicationConfigLastChangeTime_Object=MibScalar
fpuGeneralFpuApplicationConfigLastChangeTime=_FpuGeneralFpuApplicationConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,66,2,1,4),_FpuGeneralFpuApplicationConfigLastChangeTime_Type())
fpuGeneralFpuApplicationConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fpuGeneralFpuApplicationConfigLastChangeTime.setStatus(_A)
_FpuGeneralFpuApplicationStateLastChangeTime_Type=DateAndTime
_FpuGeneralFpuApplicationStateLastChangeTime_Object=MibScalar
fpuGeneralFpuApplicationStateLastChangeTime=_FpuGeneralFpuApplicationStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,66,2,1,5),_FpuGeneralFpuApplicationStateLastChangeTime_Type())
fpuGeneralFpuApplicationStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fpuGeneralFpuApplicationStateLastChangeTime.setStatus(_A)
_FpuApplicationList_ObjectIdentity=ObjectIdentity
fpuApplicationList=_FpuApplicationList_ObjectIdentity((1,3,6,1,4,1,8708,2,66,2,2))
_FpuApplicationTable_Object=MibTable
fpuApplicationTable=_FpuApplicationTable_Object((1,3,6,1,4,1,8708,2,66,2,2,1))
if mibBuilder.loadTexts:fpuApplicationTable.setStatus(_A)
_FpuApplicationEntry_Object=MibTableRow
fpuApplicationEntry=_FpuApplicationEntry_Object((1,3,6,1,4,1,8708,2,66,2,2,1,1))
fpuApplicationEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:fpuApplicationEntry.setStatus(_A)
_FpuApplicationIndex_Type=Unsigned32
_FpuApplicationIndex_Object=MibTableColumn
fpuApplicationIndex=_FpuApplicationIndex_Object((1,3,6,1,4,1,8708,2,66,2,2,1,1,1),_FpuApplicationIndex_Type())
fpuApplicationIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fpuApplicationIndex.setStatus(_A)
_FpuApplicationName_Type=MgmtNameString
_FpuApplicationName_Object=MibTableColumn
fpuApplicationName=_FpuApplicationName_Object((1,3,6,1,4,1,8708,2,66,2,2,1,1,2),_FpuApplicationName_Type())
fpuApplicationName.setMaxAccess(_C)
if mibBuilder.loadTexts:fpuApplicationName.setStatus(_A)
class _FpuApplicationWavelengthBand_Type(FpuWavelengthBand):defaultValue=1550
_FpuApplicationWavelengthBand_Type.__name__=_E
_FpuApplicationWavelengthBand_Object=MibTableColumn
fpuApplicationWavelengthBand=_FpuApplicationWavelengthBand_Object((1,3,6,1,4,1,8708,2,66,2,2,1,1,3),_FpuApplicationWavelengthBand_Type())
fpuApplicationWavelengthBand.setMaxAccess('read-write')
if mibBuilder.loadTexts:fpuApplicationWavelengthBand.setStatus(_A)
fpuGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,66,1,1,1))
fpuGeneralGroupV1.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:fpuGeneralGroupV1.setStatus(_A)
fpuApplicationGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,66,1,1,2))
fpuApplicationGroupV1.setObjects(*((_B,_D),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:fpuApplicationGroupV1.setStatus(_A)
lumFpuComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,66,1,2,1))
lumFpuComplV1.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:lumFpuComplV1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_E:FpuWavelengthBand,'lumFpuMIBModule':lumFpuMIBModule,'lumFpuConfs':lumFpuConfs,'lumFpuGroups':lumFpuGroups,_M:fpuGeneralGroupV1,_N:fpuApplicationGroupV1,'lumFpuCompl':lumFpuCompl,'lumFpuComplV1':lumFpuComplV1,'lumFpuMIBObjects':lumFpuMIBObjects,'fpuGeneral':fpuGeneral,_F:fpuGeneralConfigLastChangeTime,_G:fpuGeneralStateLastChangeTime,_H:fpuGeneralFpuApplicationTableSize,_I:fpuGeneralFpuApplicationConfigLastChangeTime,_J:fpuGeneralFpuApplicationStateLastChangeTime,'fpuApplicationList':fpuApplicationList,'fpuApplicationTable':fpuApplicationTable,'fpuApplicationEntry':fpuApplicationEntry,_D:fpuApplicationIndex,_K:fpuApplicationName,_L:fpuApplicationWavelengthBand})