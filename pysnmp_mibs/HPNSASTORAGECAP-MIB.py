_L='hpnsaSCHistIndex'
_K='hpnsaSCHistDriveIndex'
_J='optional'
_I='hpnsaSCDrvIndex'
_H='hpnsaSCAgentIndex'
_G='DisplayString'
_F='OctetString'
_E='HPNSASTORAGECAP-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_Hpnsa_ObjectIdentity=ObjectIdentity
hpnsa=_Hpnsa_ObjectIdentity((1,3,6,1,4,1,11,2,23))
_HpnsaStorageCap_ObjectIdentity=ObjectIdentity
hpnsaStorageCap=_HpnsaStorageCap_ObjectIdentity((1,3,6,1,4,1,11,2,23,15))
_HpnsaSCMibRev_ObjectIdentity=ObjectIdentity
hpnsaSCMibRev=_HpnsaSCMibRev_ObjectIdentity((1,3,6,1,4,1,11,2,23,15,1))
class _HpnsaSCMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnsaSCMibRevMajor_Type.__name__=_C
_HpnsaSCMibRevMajor_Object=MibScalar
hpnsaSCMibRevMajor=_HpnsaSCMibRevMajor_Object((1,3,6,1,4,1,11,2,23,15,1,1),_HpnsaSCMibRevMajor_Type())
hpnsaSCMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSCMibRevMajor.setStatus(_A)
class _HpnsaSCMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaSCMibRevMinor_Type.__name__=_C
_HpnsaSCMibRevMinor_Object=MibScalar
hpnsaSCMibRevMinor=_HpnsaSCMibRevMinor_Object((1,3,6,1,4,1,11,2,23,15,1,2),_HpnsaSCMibRevMinor_Type())
hpnsaSCMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSCMibRevMinor.setStatus(_A)
_HpnsaSCAgent_ObjectIdentity=ObjectIdentity
hpnsaSCAgent=_HpnsaSCAgent_ObjectIdentity((1,3,6,1,4,1,11,2,23,15,2))
_HpnsaSCAgentTable_Object=MibTable
hpnsaSCAgentTable=_HpnsaSCAgentTable_Object((1,3,6,1,4,1,11,2,23,15,2,1))
if mibBuilder.loadTexts:hpnsaSCAgentTable.setStatus(_A)
_HpnsaSCAgentEntry_Object=MibTableRow
hpnsaSCAgentEntry=_HpnsaSCAgentEntry_Object((1,3,6,1,4,1,11,2,23,15,2,1,1))
hpnsaSCAgentEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:hpnsaSCAgentEntry.setStatus(_A)
class _HpnsaSCAgentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaSCAgentIndex_Type.__name__=_C
_HpnsaSCAgentIndex_Object=MibTableColumn
hpnsaSCAgentIndex=_HpnsaSCAgentIndex_Object((1,3,6,1,4,1,11,2,23,15,2,1,1,1),_HpnsaSCAgentIndex_Type())
hpnsaSCAgentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSCAgentIndex.setStatus(_A)
class _HpnsaSCAgentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaSCAgentName_Type.__name__=_G
_HpnsaSCAgentName_Object=MibTableColumn
hpnsaSCAgentName=_HpnsaSCAgentName_Object((1,3,6,1,4,1,11,2,23,15,2,1,1,2),_HpnsaSCAgentName_Type())
hpnsaSCAgentName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSCAgentName.setStatus(_A)
class _HpnsaSCAgentVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_HpnsaSCAgentVersion_Type.__name__=_G
_HpnsaSCAgentVersion_Object=MibTableColumn
hpnsaSCAgentVersion=_HpnsaSCAgentVersion_Object((1,3,6,1,4,1,11,2,23,15,2,1,1,3),_HpnsaSCAgentVersion_Type())
hpnsaSCAgentVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSCAgentVersion.setStatus(_A)
class _HpnsaSCAgentDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnsaSCAgentDate_Type.__name__=_F
_HpnsaSCAgentDate_Object=MibTableColumn
hpnsaSCAgentDate=_HpnsaSCAgentDate_Object((1,3,6,1,4,1,11,2,23,15,2,1,1,4),_HpnsaSCAgentDate_Type())
hpnsaSCAgentDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSCAgentDate.setStatus(_A)
_HpnsaSCDrv_ObjectIdentity=ObjectIdentity
hpnsaSCDrv=_HpnsaSCDrv_ObjectIdentity((1,3,6,1,4,1,11,2,23,15,3))
_HpnsaSCDrvNumOfDrives_Type=Integer32
_HpnsaSCDrvNumOfDrives_Object=MibScalar
hpnsaSCDrvNumOfDrives=_HpnsaSCDrvNumOfDrives_Object((1,3,6,1,4,1,11,2,23,15,3,1),_HpnsaSCDrvNumOfDrives_Type())
hpnsaSCDrvNumOfDrives.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSCDrvNumOfDrives.setStatus(_A)
_HpnsaSCDrvTable_Object=MibTable
hpnsaSCDrvTable=_HpnsaSCDrvTable_Object((1,3,6,1,4,1,11,2,23,15,3,2))
if mibBuilder.loadTexts:hpnsaSCDrvTable.setStatus(_A)
_HpnsaSCDrvEntry_Object=MibTableRow
hpnsaSCDrvEntry=_HpnsaSCDrvEntry_Object((1,3,6,1,4,1,11,2,23,15,3,2,1))
hpnsaSCDrvEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:hpnsaSCDrvEntry.setStatus(_A)
_HpnsaSCDrvIndex_Type=Integer32
_HpnsaSCDrvIndex_Object=MibTableColumn
hpnsaSCDrvIndex=_HpnsaSCDrvIndex_Object((1,3,6,1,4,1,11,2,23,15,3,2,1,1),_HpnsaSCDrvIndex_Type())
hpnsaSCDrvIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSCDrvIndex.setStatus(_A)
_HpnsaSCDrvName_Type=DisplayString
_HpnsaSCDrvName_Object=MibTableColumn
hpnsaSCDrvName=_HpnsaSCDrvName_Object((1,3,6,1,4,1,11,2,23,15,3,2,1,2),_HpnsaSCDrvName_Type())
hpnsaSCDrvName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSCDrvName.setStatus(_A)
class _HpnsaSCDrvTrapsEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_HpnsaSCDrvTrapsEnabled_Type.__name__=_C
_HpnsaSCDrvTrapsEnabled_Object=MibTableColumn
hpnsaSCDrvTrapsEnabled=_HpnsaSCDrvTrapsEnabled_Object((1,3,6,1,4,1,11,2,23,15,3,2,1,3),_HpnsaSCDrvTrapsEnabled_Type())
hpnsaSCDrvTrapsEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaSCDrvTrapsEnabled.setStatus(_A)
_HpnsaSCDrvTrapsPollTime_Type=Integer32
_HpnsaSCDrvTrapsPollTime_Object=MibTableColumn
hpnsaSCDrvTrapsPollTime=_HpnsaSCDrvTrapsPollTime_Object((1,3,6,1,4,1,11,2,23,15,3,2,1,4),_HpnsaSCDrvTrapsPollTime_Type())
hpnsaSCDrvTrapsPollTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaSCDrvTrapsPollTime.setStatus(_A)
_HpnsaSCDrvHistSampleTime_Type=Integer32
_HpnsaSCDrvHistSampleTime_Object=MibTableColumn
hpnsaSCDrvHistSampleTime=_HpnsaSCDrvHistSampleTime_Object((1,3,6,1,4,1,11,2,23,15,3,2,1,5),_HpnsaSCDrvHistSampleTime_Type())
hpnsaSCDrvHistSampleTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaSCDrvHistSampleTime.setStatus(_A)
_HpnsaSCDrvLoThreshold_Type=Integer32
_HpnsaSCDrvLoThreshold_Object=MibTableColumn
hpnsaSCDrvLoThreshold=_HpnsaSCDrvLoThreshold_Object((1,3,6,1,4,1,11,2,23,15,3,2,1,6),_HpnsaSCDrvLoThreshold_Type())
hpnsaSCDrvLoThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaSCDrvLoThreshold.setStatus(_A)
_HpnsaSCDrvWarnThreshold_Type=Integer32
_HpnsaSCDrvWarnThreshold_Object=MibTableColumn
hpnsaSCDrvWarnThreshold=_HpnsaSCDrvWarnThreshold_Object((1,3,6,1,4,1,11,2,23,15,3,2,1,7),_HpnsaSCDrvWarnThreshold_Type())
hpnsaSCDrvWarnThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaSCDrvWarnThreshold.setStatus(_A)
_HpnsaSCDrvCritThreshold_Type=Integer32
_HpnsaSCDrvCritThreshold_Object=MibTableColumn
hpnsaSCDrvCritThreshold=_HpnsaSCDrvCritThreshold_Object((1,3,6,1,4,1,11,2,23,15,3,2,1,8),_HpnsaSCDrvCritThreshold_Type())
hpnsaSCDrvCritThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaSCDrvCritThreshold.setStatus(_A)
_HpnsaSCDrvTotalNumDirEntries_Type=Integer32
_HpnsaSCDrvTotalNumDirEntries_Object=MibTableColumn
hpnsaSCDrvTotalNumDirEntries=_HpnsaSCDrvTotalNumDirEntries_Object((1,3,6,1,4,1,11,2,23,15,3,2,1,9),_HpnsaSCDrvTotalNumDirEntries_Type())
hpnsaSCDrvTotalNumDirEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSCDrvTotalNumDirEntries.setStatus(_J)
_HpnsaSCDrvTotalNumDirEntriesUsed_Type=Integer32
_HpnsaSCDrvTotalNumDirEntriesUsed_Object=MibTableColumn
hpnsaSCDrvTotalNumDirEntriesUsed=_HpnsaSCDrvTotalNumDirEntriesUsed_Object((1,3,6,1,4,1,11,2,23,15,3,2,1,10),_HpnsaSCDrvTotalNumDirEntriesUsed_Type())
hpnsaSCDrvTotalNumDirEntriesUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSCDrvTotalNumDirEntriesUsed.setStatus(_J)
_HpnsaSCDrvCurrentTotal_Type=Integer32
_HpnsaSCDrvCurrentTotal_Object=MibTableColumn
hpnsaSCDrvCurrentTotal=_HpnsaSCDrvCurrentTotal_Object((1,3,6,1,4,1,11,2,23,15,3,2,1,11),_HpnsaSCDrvCurrentTotal_Type())
hpnsaSCDrvCurrentTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSCDrvCurrentTotal.setStatus(_A)
_HpnsaSCDrvCurrentAvailable_Type=Integer32
_HpnsaSCDrvCurrentAvailable_Object=MibTableColumn
hpnsaSCDrvCurrentAvailable=_HpnsaSCDrvCurrentAvailable_Object((1,3,6,1,4,1,11,2,23,15,3,2,1,12),_HpnsaSCDrvCurrentAvailable_Type())
hpnsaSCDrvCurrentAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSCDrvCurrentAvailable.setStatus(_A)
_HpnsaSCDrvNumOfSamples_Type=Integer32
_HpnsaSCDrvNumOfSamples_Object=MibTableColumn
hpnsaSCDrvNumOfSamples=_HpnsaSCDrvNumOfSamples_Object((1,3,6,1,4,1,11,2,23,15,3,2,1,13),_HpnsaSCDrvNumOfSamples_Type())
hpnsaSCDrvNumOfSamples.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSCDrvNumOfSamples.setStatus(_A)
_HpnsaSCDrvClearHist_Type=Integer32
_HpnsaSCDrvClearHist_Object=MibTableColumn
hpnsaSCDrvClearHist=_HpnsaSCDrvClearHist_Object((1,3,6,1,4,1,11,2,23,15,3,2,1,14),_HpnsaSCDrvClearHist_Type())
hpnsaSCDrvClearHist.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaSCDrvClearHist.setStatus(_A)
_HpnsaSCHist_ObjectIdentity=ObjectIdentity
hpnsaSCHist=_HpnsaSCHist_ObjectIdentity((1,3,6,1,4,1,11,2,23,15,4))
_HpnsaSCHistTable_Object=MibTable
hpnsaSCHistTable=_HpnsaSCHistTable_Object((1,3,6,1,4,1,11,2,23,15,4,1))
if mibBuilder.loadTexts:hpnsaSCHistTable.setStatus(_A)
_HpnsaSCHistEntry_Object=MibTableRow
hpnsaSCHistEntry=_HpnsaSCHistEntry_Object((1,3,6,1,4,1,11,2,23,15,4,1,1))
hpnsaSCHistEntry.setIndexNames((0,_E,_K),(0,_E,_L))
if mibBuilder.loadTexts:hpnsaSCHistEntry.setStatus(_A)
class _HpnsaSCHistDriveIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaSCHistDriveIndex_Type.__name__=_C
_HpnsaSCHistDriveIndex_Object=MibTableColumn
hpnsaSCHistDriveIndex=_HpnsaSCHistDriveIndex_Object((1,3,6,1,4,1,11,2,23,15,4,1,1,1),_HpnsaSCHistDriveIndex_Type())
hpnsaSCHistDriveIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSCHistDriveIndex.setStatus(_A)
class _HpnsaSCHistIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,400))
_HpnsaSCHistIndex_Type.__name__=_C
_HpnsaSCHistIndex_Object=MibTableColumn
hpnsaSCHistIndex=_HpnsaSCHistIndex_Object((1,3,6,1,4,1,11,2,23,15,4,1,1,2),_HpnsaSCHistIndex_Type())
hpnsaSCHistIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSCHistIndex.setStatus(_A)
class _HpnsaSCHistSample_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(14,14));fixedLength=14
_HpnsaSCHistSample_Type.__name__=_F
_HpnsaSCHistSample_Object=MibTableColumn
hpnsaSCHistSample=_HpnsaSCHistSample_Object((1,3,6,1,4,1,11,2,23,15,4,1,1,3),_HpnsaSCHistSample_Type())
hpnsaSCHistSample.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSCHistSample.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hp':hp,'nm':nm,'hpnsa':hpnsa,'hpnsaStorageCap':hpnsaStorageCap,'hpnsaSCMibRev':hpnsaSCMibRev,'hpnsaSCMibRevMajor':hpnsaSCMibRevMajor,'hpnsaSCMibRevMinor':hpnsaSCMibRevMinor,'hpnsaSCAgent':hpnsaSCAgent,'hpnsaSCAgentTable':hpnsaSCAgentTable,'hpnsaSCAgentEntry':hpnsaSCAgentEntry,_H:hpnsaSCAgentIndex,'hpnsaSCAgentName':hpnsaSCAgentName,'hpnsaSCAgentVersion':hpnsaSCAgentVersion,'hpnsaSCAgentDate':hpnsaSCAgentDate,'hpnsaSCDrv':hpnsaSCDrv,'hpnsaSCDrvNumOfDrives':hpnsaSCDrvNumOfDrives,'hpnsaSCDrvTable':hpnsaSCDrvTable,'hpnsaSCDrvEntry':hpnsaSCDrvEntry,_I:hpnsaSCDrvIndex,'hpnsaSCDrvName':hpnsaSCDrvName,'hpnsaSCDrvTrapsEnabled':hpnsaSCDrvTrapsEnabled,'hpnsaSCDrvTrapsPollTime':hpnsaSCDrvTrapsPollTime,'hpnsaSCDrvHistSampleTime':hpnsaSCDrvHistSampleTime,'hpnsaSCDrvLoThreshold':hpnsaSCDrvLoThreshold,'hpnsaSCDrvWarnThreshold':hpnsaSCDrvWarnThreshold,'hpnsaSCDrvCritThreshold':hpnsaSCDrvCritThreshold,'hpnsaSCDrvTotalNumDirEntries':hpnsaSCDrvTotalNumDirEntries,'hpnsaSCDrvTotalNumDirEntriesUsed':hpnsaSCDrvTotalNumDirEntriesUsed,'hpnsaSCDrvCurrentTotal':hpnsaSCDrvCurrentTotal,'hpnsaSCDrvCurrentAvailable':hpnsaSCDrvCurrentAvailable,'hpnsaSCDrvNumOfSamples':hpnsaSCDrvNumOfSamples,'hpnsaSCDrvClearHist':hpnsaSCDrvClearHist,'hpnsaSCHist':hpnsaSCHist,'hpnsaSCHistTable':hpnsaSCHistTable,'hpnsaSCHistEntry':hpnsaSCHistEntry,_K:hpnsaSCHistDriveIndex,_L:hpnsaSCHistIndex,'hpnsaSCHistSample':hpnsaSCHistSample})