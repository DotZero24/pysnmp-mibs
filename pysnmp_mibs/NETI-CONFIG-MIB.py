_G='configLocalIndex'
_F='NETI-CONFIG-MIB'
_E='read-write'
_D='read-create'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netiExperimentalGeneric,=mibBuilder.importSymbols('NETI-COMMON-MIB','netiExperimentalGeneric')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
netiConfigMIB=ModuleIdentity((1,3,6,1,4,1,2928,6,2,7))
_NetiConfigMIBObjects_ObjectIdentity=ObjectIdentity
netiConfigMIBObjects=_NetiConfigMIBObjects_ObjectIdentity((1,3,6,1,4,1,2928,6,2,7,1))
_ConfigStatusGroup_ObjectIdentity=ObjectIdentity
configStatusGroup=_ConfigStatusGroup_ObjectIdentity((1,3,6,1,4,1,2928,6,2,7,1,1))
_ConfigStatusIsCurrentUnsaved_Type=TruthValue
_ConfigStatusIsCurrentUnsaved_Object=MibScalar
configStatusIsCurrentUnsaved=_ConfigStatusIsCurrentUnsaved_Object((1,3,6,1,4,1,2928,6,2,7,1,1,1),_ConfigStatusIsCurrentUnsaved_Type())
configStatusIsCurrentUnsaved.setMaxAccess(_B)
if mibBuilder.loadTexts:configStatusIsCurrentUnsaved.setStatus(_A)
_ConfigStatusCurrentLastChangedTime_Type=DateAndTime
_ConfigStatusCurrentLastChangedTime_Object=MibScalar
configStatusCurrentLastChangedTime=_ConfigStatusCurrentLastChangedTime_Object((1,3,6,1,4,1,2928,6,2,7,1,1,2),_ConfigStatusCurrentLastChangedTime_Type())
configStatusCurrentLastChangedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:configStatusCurrentLastChangedTime.setStatus(_A)
_ConfigLocalGroup_ObjectIdentity=ObjectIdentity
configLocalGroup=_ConfigLocalGroup_ObjectIdentity((1,3,6,1,4,1,2928,6,2,7,1,2))
_ConfigLocalTableLastChangedTime_Type=DateAndTime
_ConfigLocalTableLastChangedTime_Object=MibScalar
configLocalTableLastChangedTime=_ConfigLocalTableLastChangedTime_Object((1,3,6,1,4,1,2928,6,2,7,1,2,2),_ConfigLocalTableLastChangedTime_Type())
configLocalTableLastChangedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:configLocalTableLastChangedTime.setStatus(_A)
_ConfigLocalTableNrOfConfigs_Type=Gauge32
_ConfigLocalTableNrOfConfigs_Object=MibScalar
configLocalTableNrOfConfigs=_ConfigLocalTableNrOfConfigs_Object((1,3,6,1,4,1,2928,6,2,7,1,2,3),_ConfigLocalTableNrOfConfigs_Type())
configLocalTableNrOfConfigs.setMaxAccess(_B)
if mibBuilder.loadTexts:configLocalTableNrOfConfigs.setStatus(_A)
_ConfigLocalTable_Object=MibTable
configLocalTable=_ConfigLocalTable_Object((1,3,6,1,4,1,2928,6,2,7,1,2,4))
if mibBuilder.loadTexts:configLocalTable.setStatus(_A)
_ConfigLocalEntry_Object=MibTableRow
configLocalEntry=_ConfigLocalEntry_Object((1,3,6,1,4,1,2928,6,2,7,1,2,4,1))
configLocalEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:configLocalEntry.setStatus(_A)
class _ConfigLocalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ConfigLocalIndex_Type.__name__=_C
_ConfigLocalIndex_Object=MibTableColumn
configLocalIndex=_ConfigLocalIndex_Object((1,3,6,1,4,1,2928,6,2,7,1,2,4,1,1),_ConfigLocalIndex_Type())
configLocalIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:configLocalIndex.setStatus(_A)
_ConfigLocalName_Type=DisplayString
_ConfigLocalName_Object=MibTableColumn
configLocalName=_ConfigLocalName_Object((1,3,6,1,4,1,2928,6,2,7,1,2,4,1,2),_ConfigLocalName_Type())
configLocalName.setMaxAccess(_D)
if mibBuilder.loadTexts:configLocalName.setStatus(_A)
_ConfigLocalDescription_Type=DisplayString
_ConfigLocalDescription_Object=MibTableColumn
configLocalDescription=_ConfigLocalDescription_Object((1,3,6,1,4,1,2928,6,2,7,1,2,4,1,3),_ConfigLocalDescription_Type())
configLocalDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:configLocalDescription.setStatus(_A)
_ConfigLocalCreatedTime_Type=DateAndTime
_ConfigLocalCreatedTime_Object=MibTableColumn
configLocalCreatedTime=_ConfigLocalCreatedTime_Object((1,3,6,1,4,1,2928,6,2,7,1,2,4,1,4),_ConfigLocalCreatedTime_Type())
configLocalCreatedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:configLocalCreatedTime.setStatus(_A)
class _ConfigLocalSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ConfigLocalSize_Type.__name__=_C
_ConfigLocalSize_Object=MibTableColumn
configLocalSize=_ConfigLocalSize_Object((1,3,6,1,4,1,2928,6,2,7,1,2,4,1,5),_ConfigLocalSize_Type())
configLocalSize.setMaxAccess(_B)
if mibBuilder.loadTexts:configLocalSize.setStatus(_A)
class _ConfigLocalAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_ConfigLocalAdminStatus_Type.__name__=_C
_ConfigLocalAdminStatus_Object=MibTableColumn
configLocalAdminStatus=_ConfigLocalAdminStatus_Object((1,3,6,1,4,1,2928,6,2,7,1,2,4,1,6),_ConfigLocalAdminStatus_Type())
configLocalAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:configLocalAdminStatus.setStatus(_A)
_ConfigLocalRowStatus_Type=RowStatus
_ConfigLocalRowStatus_Object=MibTableColumn
configLocalRowStatus=_ConfigLocalRowStatus_Object((1,3,6,1,4,1,2928,6,2,7,1,2,4,1,7),_ConfigLocalRowStatus_Type())
configLocalRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:configLocalRowStatus.setStatus(_A)
_ConfigBackupGroup_ObjectIdentity=ObjectIdentity
configBackupGroup=_ConfigBackupGroup_ObjectIdentity((1,3,6,1,4,1,2928,6,2,7,1,3))
class _ConfigBackupOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('idle',1),('writeCurrentToLocal',2)))
_ConfigBackupOperation_Type.__name__=_C
_ConfigBackupOperation_Object=MibScalar
configBackupOperation=_ConfigBackupOperation_Object((1,3,6,1,4,1,2928,6,2,7,1,3,1),_ConfigBackupOperation_Type())
configBackupOperation.setMaxAccess(_E)
if mibBuilder.loadTexts:configBackupOperation.setStatus(_A)
class _ConfigBackupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('idle',1),('inProgress',2),('failed',3),('ready',4)))
_ConfigBackupStatus_Type.__name__=_C
_ConfigBackupStatus_Object=MibScalar
configBackupStatus=_ConfigBackupStatus_Object((1,3,6,1,4,1,2928,6,2,7,1,3,2),_ConfigBackupStatus_Type())
configBackupStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:configBackupStatus.setStatus(_A)
_ConfigBackupName_Type=DisplayString
_ConfigBackupName_Object=MibScalar
configBackupName=_ConfigBackupName_Object((1,3,6,1,4,1,2928,6,2,7,1,3,3),_ConfigBackupName_Type())
configBackupName.setMaxAccess(_E)
if mibBuilder.loadTexts:configBackupName.setStatus(_A)
_ConfigBackupDescription_Type=DisplayString
_ConfigBackupDescription_Object=MibScalar
configBackupDescription=_ConfigBackupDescription_Object((1,3,6,1,4,1,2928,6,2,7,1,3,4),_ConfigBackupDescription_Type())
configBackupDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:configBackupDescription.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'netiConfigMIB':netiConfigMIB,'netiConfigMIBObjects':netiConfigMIBObjects,'configStatusGroup':configStatusGroup,'configStatusIsCurrentUnsaved':configStatusIsCurrentUnsaved,'configStatusCurrentLastChangedTime':configStatusCurrentLastChangedTime,'configLocalGroup':configLocalGroup,'configLocalTableLastChangedTime':configLocalTableLastChangedTime,'configLocalTableNrOfConfigs':configLocalTableNrOfConfigs,'configLocalTable':configLocalTable,'configLocalEntry':configLocalEntry,_G:configLocalIndex,'configLocalName':configLocalName,'configLocalDescription':configLocalDescription,'configLocalCreatedTime':configLocalCreatedTime,'configLocalSize':configLocalSize,'configLocalAdminStatus':configLocalAdminStatus,'configLocalRowStatus':configLocalRowStatus,'configBackupGroup':configBackupGroup,'configBackupOperation':configBackupOperation,'configBackupStatus':configBackupStatus,'configBackupName':configBackupName,'configBackupDescription':configBackupDescription})