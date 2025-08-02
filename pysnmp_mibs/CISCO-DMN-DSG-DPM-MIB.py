_Q='dpmAlignedPMTRow'
_P='dpmAlignedPMTPEID'
_O='dpmAlignedPMTInstanceID'
_N='dpmPIDMapIndex'
_M='dpmPeMappingPEID'
_L='dpmPeMappingInstanceID'
_K='dpmGblCfgInstanceID'
_J='DisplayString'
_I='pwRC'
_H='regeneration'
_G='CISCO-DMN-DSG-DPM-MIB'
_F='read-only'
_E='pass'
_D='drop'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','RowStatus','TextualConvention')
ciscoDSGDPM=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,36))
if mibBuilder.loadTexts:ciscoDSGDPM.setRevisions(('2012-03-12 17:00',))
_DpmInfo_ObjectIdentity=ObjectIdentity
dpmInfo=_DpmInfo_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,36,1))
class _DpmRegenerate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('always',1),('asNeeded',2)))
_DpmRegenerate_Type.__name__=_B
_DpmRegenerate_Object=MibScalar
dpmRegenerate=_DpmRegenerate_Object((1,3,6,1,4,1,1429,2,2,5,36,1,1),_DpmRegenerate_Type())
dpmRegenerate.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmRegenerate.setStatus(_A)
_DpmTable_ObjectIdentity=ObjectIdentity
dpmTable=_DpmTable_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,36,2))
_DpmGblCfgTable_Object=MibTable
dpmGblCfgTable=_DpmGblCfgTable_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1))
if mibBuilder.loadTexts:dpmGblCfgTable.setStatus(_A)
_DpmGblCfgEntry_Object=MibTableRow
dpmGblCfgEntry=_DpmGblCfgEntry_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1))
dpmGblCfgEntry.setIndexNames((0,_G,_K))
if mibBuilder.loadTexts:dpmGblCfgEntry.setStatus(_A)
class _DpmGblCfgInstanceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_DpmGblCfgInstanceID_Type.__name__=_B
_DpmGblCfgInstanceID_Object=MibTableColumn
dpmGblCfgInstanceID=_DpmGblCfgInstanceID_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,1),_DpmGblCfgInstanceID_Type())
dpmGblCfgInstanceID.setMaxAccess(_F)
if mibBuilder.loadTexts:dpmGblCfgInstanceID.setStatus(_A)
class _DpmGblCfgInstanceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DpmGblCfgInstanceName_Type.__name__=_J
_DpmGblCfgInstanceName_Object=MibTableColumn
dpmGblCfgInstanceName=_DpmGblCfgInstanceName_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,2),_DpmGblCfgInstanceName_Type())
dpmGblCfgInstanceName.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgInstanceName.setStatus(_A)
class _DpmGblCfgMapMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('svcID',1),('svcIDAndPID',2)))
_DpmGblCfgMapMode_Type.__name__=_B
_DpmGblCfgMapMode_Object=MibTableColumn
dpmGblCfgMapMode=_DpmGblCfgMapMode_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,3),_DpmGblCfgMapMode_Type())
dpmGblCfgMapMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgMapMode.setStatus(_A)
class _DpmGblCfgDupMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('psiRemap',1),('packetCopy',2)))
_DpmGblCfgDupMethod_Type.__name__=_B
_DpmGblCfgDupMethod_Object=MibTableColumn
dpmGblCfgDupMethod=_DpmGblCfgDupMethod_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,4),_DpmGblCfgDupMethod_Type())
dpmGblCfgDupMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgDupMethod.setStatus(_A)
class _DpmGblCfgRegenRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('saStandard',1),('mpegMinimum',2),('auto',3)))
_DpmGblCfgRegenRate_Type.__name__=_B
_DpmGblCfgRegenRate_Object=MibTableColumn
dpmGblCfgRegenRate=_DpmGblCfgRegenRate_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,5),_DpmGblCfgRegenRate_Type())
dpmGblCfgRegenRate.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgRegenRate.setStatus(_A)
class _DpmGblCfgUnrefContent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),('modeI',3)))
_DpmGblCfgUnrefContent_Type.__name__=_B
_DpmGblCfgUnrefContent_Object=MibTableColumn
dpmGblCfgUnrefContent=_DpmGblCfgUnrefContent_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,6),_DpmGblCfgUnrefContent_Type())
dpmGblCfgUnrefContent.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgUnrefContent.setStatus(_A)
class _DpmGblCfgPSIOutput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dropAll',1),('passAll',2),('ctlByTable',3)))
_DpmGblCfgPSIOutput_Type.__name__=_B
_DpmGblCfgPSIOutput_Object=MibTableColumn
dpmGblCfgPSIOutput=_DpmGblCfgPSIOutput_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,7),_DpmGblCfgPSIOutput_Type())
dpmGblCfgPSIOutput.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSIOutput.setStatus(_A)
class _DpmGblCfgSVCIDOutput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('validChannel',1),('allChannel',2)))
_DpmGblCfgSVCIDOutput_Type.__name__=_B
_DpmGblCfgSVCIDOutput_Object=MibTableColumn
dpmGblCfgSVCIDOutput=_DpmGblCfgSVCIDOutput_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,8),_DpmGblCfgSVCIDOutput_Type())
dpmGblCfgSVCIDOutput.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgSVCIDOutput.setStatus(_A)
class _DpmGblCfgPSIPAT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_H,3)))
_DpmGblCfgPSIPAT_Type.__name__=_B
_DpmGblCfgPSIPAT_Object=MibTableColumn
dpmGblCfgPSIPAT=_DpmGblCfgPSIPAT_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,9),_DpmGblCfgPSIPAT_Type())
dpmGblCfgPSIPAT.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSIPAT.setStatus(_A)
class _DpmGblCfgPSICAT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_H,3)))
_DpmGblCfgPSICAT_Type.__name__=_B
_DpmGblCfgPSICAT_Object=MibTableColumn
dpmGblCfgPSICAT=_DpmGblCfgPSICAT_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,10),_DpmGblCfgPSICAT_Type())
dpmGblCfgPSICAT.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSICAT.setStatus(_A)
class _DpmGblCfgPSIPMT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_H,3)))
_DpmGblCfgPSIPMT_Type.__name__=_B
_DpmGblCfgPSIPMT_Object=MibTableColumn
dpmGblCfgPSIPMT=_DpmGblCfgPSIPMT_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,11),_DpmGblCfgPSIPMT_Type())
dpmGblCfgPSIPMT.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSIPMT.setStatus(_A)
class _DpmGblCfgPSITSDT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DpmGblCfgPSITSDT_Type.__name__=_B
_DpmGblCfgPSITSDT_Object=MibTableColumn
dpmGblCfgPSITSDT=_DpmGblCfgPSITSDT_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,12),_DpmGblCfgPSITSDT_Type())
dpmGblCfgPSITSDT.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSITSDT.setStatus(_A)
class _DpmGblCfgPSINIT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_H,3)))
_DpmGblCfgPSINIT_Type.__name__=_B
_DpmGblCfgPSINIT_Object=MibTableColumn
dpmGblCfgPSINIT=_DpmGblCfgPSINIT_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,13),_DpmGblCfgPSINIT_Type())
dpmGblCfgPSINIT.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSINIT.setStatus(_A)
class _DpmGblCfgPSINITO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*((_D,1),(_E,2),(_I,4)))
_DpmGblCfgPSINITO_Type.__name__=_B
_DpmGblCfgPSINITO_Object=MibTableColumn
dpmGblCfgPSINITO=_DpmGblCfgPSINITO_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,14),_DpmGblCfgPSINITO_Type())
dpmGblCfgPSINITO.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSINITO.setStatus(_A)
class _DpmGblCfgPSISDT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_E,2),(_H,3),(_I,4)))
_DpmGblCfgPSISDT_Type.__name__=_B
_DpmGblCfgPSISDT_Object=MibTableColumn
dpmGblCfgPSISDT=_DpmGblCfgPSISDT_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,15),_DpmGblCfgPSISDT_Type())
dpmGblCfgPSISDT.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSISDT.setStatus(_A)
class _DpmGblCfgPSISDTO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*((_D,1),(_E,2),(_I,4)))
_DpmGblCfgPSISDTO_Type.__name__=_B
_DpmGblCfgPSISDTO_Object=MibTableColumn
dpmGblCfgPSISDTO=_DpmGblCfgPSISDTO_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,16),_DpmGblCfgPSISDTO_Type())
dpmGblCfgPSISDTO.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSISDTO.setStatus(_A)
class _DpmGblCfgPSIBAT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*((_D,1),(_E,2),(_I,4)))
_DpmGblCfgPSIBAT_Type.__name__=_B
_DpmGblCfgPSIBAT_Object=MibTableColumn
dpmGblCfgPSIBAT=_DpmGblCfgPSIBAT_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,17),_DpmGblCfgPSIBAT_Type())
dpmGblCfgPSIBAT.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSIBAT.setStatus(_A)
class _DpmGblCfgPSIEIT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DpmGblCfgPSIEIT_Type.__name__=_B
_DpmGblCfgPSIEIT_Object=MibTableColumn
dpmGblCfgPSIEIT=_DpmGblCfgPSIEIT_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,18),_DpmGblCfgPSIEIT_Type())
dpmGblCfgPSIEIT.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSIEIT.setStatus(_A)
class _DpmGblCfgPSITDT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DpmGblCfgPSITDT_Type.__name__=_B
_DpmGblCfgPSITDT_Object=MibTableColumn
dpmGblCfgPSITDT=_DpmGblCfgPSITDT_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,19),_DpmGblCfgPSITDT_Type())
dpmGblCfgPSITDT.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSITDT.setStatus(_A)
class _DpmGblCfgPSIST_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DpmGblCfgPSIST_Type.__name__=_B
_DpmGblCfgPSIST_Object=MibTableColumn
dpmGblCfgPSIST=_DpmGblCfgPSIST_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,20),_DpmGblCfgPSIST_Type())
dpmGblCfgPSIST.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSIST.setStatus(_A)
class _DpmGblCfgPSIRST_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DpmGblCfgPSIRST_Type.__name__=_B
_DpmGblCfgPSIRST_Object=MibTableColumn
dpmGblCfgPSIRST=_DpmGblCfgPSIRST_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,21),_DpmGblCfgPSIRST_Type())
dpmGblCfgPSIRST.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSIRST.setStatus(_A)
class _DpmGblCfgPSITOT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DpmGblCfgPSITOT_Type.__name__=_B
_DpmGblCfgPSITOT_Object=MibTableColumn
dpmGblCfgPSITOT=_DpmGblCfgPSITOT_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,22),_DpmGblCfgPSITOT_Type())
dpmGblCfgPSITOT.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSITOT.setStatus(_A)
class _DpmGblCfgPSIDIT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DpmGblCfgPSIDIT_Type.__name__=_B
_DpmGblCfgPSIDIT_Object=MibTableColumn
dpmGblCfgPSIDIT=_DpmGblCfgPSIDIT_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,23),_DpmGblCfgPSIDIT_Type())
dpmGblCfgPSIDIT.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSIDIT.setStatus(_A)
class _DpmGblCfgPSISIT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DpmGblCfgPSISIT_Type.__name__=_B
_DpmGblCfgPSISIT_Object=MibTableColumn
dpmGblCfgPSISIT=_DpmGblCfgPSISIT_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,24),_DpmGblCfgPSISIT_Type())
dpmGblCfgPSISIT.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSISIT.setStatus(_A)
class _DpmGblCfgPSIECM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DpmGblCfgPSIECM_Type.__name__=_B
_DpmGblCfgPSIECM_Object=MibTableColumn
dpmGblCfgPSIECM=_DpmGblCfgPSIECM_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,25),_DpmGblCfgPSIECM_Type())
dpmGblCfgPSIECM.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSIECM.setStatus(_A)
class _DpmGblCfgPSIEMM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DpmGblCfgPSIEMM_Type.__name__=_B
_DpmGblCfgPSIEMM_Object=MibTableColumn
dpmGblCfgPSIEMM=_DpmGblCfgPSIEMM_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,26),_DpmGblCfgPSIEMM_Type())
dpmGblCfgPSIEMM.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSIEMM.setStatus(_A)
class _DpmGblCfgPSIDRT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DpmGblCfgPSIDRT_Type.__name__=_B
_DpmGblCfgPSIDRT_Object=MibTableColumn
dpmGblCfgPSIDRT=_DpmGblCfgPSIDRT_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,27),_DpmGblCfgPSIDRT_Type())
dpmGblCfgPSIDRT.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSIDRT.setStatus(_A)
class _DpmGblCfgPSICDT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DpmGblCfgPSICDT_Type.__name__=_B
_DpmGblCfgPSICDT_Object=MibTableColumn
dpmGblCfgPSICDT=_DpmGblCfgPSICDT_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,28),_DpmGblCfgPSICDT_Type())
dpmGblCfgPSICDT.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPSICDT.setStatus(_A)
class _DpmGblCfgPATPMTOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7500))
_DpmGblCfgPATPMTOffset_Type.__name__=_B
_DpmGblCfgPATPMTOffset_Object=MibTableColumn
dpmGblCfgPATPMTOffset=_DpmGblCfgPATPMTOffset_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,29),_DpmGblCfgPATPMTOffset_Type())
dpmGblCfgPATPMTOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgPATPMTOffset.setStatus(_A)
class _DpmGblCfgNITOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7500))
_DpmGblCfgNITOffset_Type.__name__=_B
_DpmGblCfgNITOffset_Object=MibTableColumn
dpmGblCfgNITOffset=_DpmGblCfgNITOffset_Object((1,3,6,1,4,1,1429,2,2,5,36,2,1,1,30),_DpmGblCfgNITOffset_Type())
dpmGblCfgNITOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmGblCfgNITOffset.setStatus(_A)
_DpmPeMappingTable_Object=MibTable
dpmPeMappingTable=_DpmPeMappingTable_Object((1,3,6,1,4,1,1429,2,2,5,36,2,2))
if mibBuilder.loadTexts:dpmPeMappingTable.setStatus(_A)
_DpmPeMappingEntry_Object=MibTableRow
dpmPeMappingEntry=_DpmPeMappingEntry_Object((1,3,6,1,4,1,1429,2,2,5,36,2,2,1))
dpmPeMappingEntry.setIndexNames((0,_G,_L),(0,_G,_M))
if mibBuilder.loadTexts:dpmPeMappingEntry.setStatus(_A)
class _DpmPeMappingInstanceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_DpmPeMappingInstanceID_Type.__name__=_B
_DpmPeMappingInstanceID_Object=MibTableColumn
dpmPeMappingInstanceID=_DpmPeMappingInstanceID_Object((1,3,6,1,4,1,1429,2,2,5,36,2,2,1,1),_DpmPeMappingInstanceID_Type())
dpmPeMappingInstanceID.setMaxAccess(_F)
if mibBuilder.loadTexts:dpmPeMappingInstanceID.setStatus(_A)
class _DpmPeMappingPEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_DpmPeMappingPEID_Type.__name__=_B
_DpmPeMappingPEID_Object=MibTableColumn
dpmPeMappingPEID=_DpmPeMappingPEID_Object((1,3,6,1,4,1,1429,2,2,5,36,2,2,1,2),_DpmPeMappingPEID_Type())
dpmPeMappingPEID.setMaxAccess(_F)
if mibBuilder.loadTexts:dpmPeMappingPEID.setStatus(_A)
class _DpmPeMappingAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_E,2),('map',3),('xcode',4)))
_DpmPeMappingAction_Type.__name__=_B
_DpmPeMappingAction_Object=MibTableColumn
dpmPeMappingAction=_DpmPeMappingAction_Object((1,3,6,1,4,1,1429,2,2,5,36,2,2,1,3),_DpmPeMappingAction_Type())
dpmPeMappingAction.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmPeMappingAction.setStatus(_A)
class _DpmPeMappingPMTPID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8191))
_DpmPeMappingPMTPID_Type.__name__=_B
_DpmPeMappingPMTPID_Object=MibTableColumn
dpmPeMappingPMTPID=_DpmPeMappingPMTPID_Object((1,3,6,1,4,1,1429,2,2,5,36,2,2,1,4),_DpmPeMappingPMTPID_Type())
dpmPeMappingPMTPID.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmPeMappingPMTPID.setStatus(_A)
class _DpmPeMappingOpChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DpmPeMappingOpChannel_Type.__name__=_B
_DpmPeMappingOpChannel_Object=MibTableColumn
dpmPeMappingOpChannel=_DpmPeMappingOpChannel_Object((1,3,6,1,4,1,1429,2,2,5,36,2,2,1,5),_DpmPeMappingOpChannel_Type())
dpmPeMappingOpChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmPeMappingOpChannel.setStatus(_A)
_DpmPIDMapTable_Object=MibTable
dpmPIDMapTable=_DpmPIDMapTable_Object((1,3,6,1,4,1,1429,2,2,5,36,2,3))
if mibBuilder.loadTexts:dpmPIDMapTable.setStatus(_A)
_DpmPIDMapEntry_Object=MibTableRow
dpmPIDMapEntry=_DpmPIDMapEntry_Object((1,3,6,1,4,1,1429,2,2,5,36,2,3,1))
dpmPIDMapEntry.setIndexNames((0,_G,_N))
if mibBuilder.loadTexts:dpmPIDMapEntry.setStatus(_A)
class _DpmPIDMapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,768))
_DpmPIDMapIndex_Type.__name__=_B
_DpmPIDMapIndex_Object=MibTableColumn
dpmPIDMapIndex=_DpmPIDMapIndex_Object((1,3,6,1,4,1,1429,2,2,5,36,2,3,1,1),_DpmPIDMapIndex_Type())
dpmPIDMapIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:dpmPIDMapIndex.setStatus(_A)
class _DpmPIDMapInstanceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_DpmPIDMapInstanceID_Type.__name__=_B
_DpmPIDMapInstanceID_Object=MibTableColumn
dpmPIDMapInstanceID=_DpmPIDMapInstanceID_Object((1,3,6,1,4,1,1429,2,2,5,36,2,3,1,2),_DpmPIDMapInstanceID_Type())
dpmPIDMapInstanceID.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmPIDMapInstanceID.setStatus(_A)
class _DpmPIDMapPEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_DpmPIDMapPEID_Type.__name__=_B
_DpmPIDMapPEID_Object=MibTableColumn
dpmPIDMapPEID=_DpmPIDMapPEID_Object((1,3,6,1,4,1,1429,2,2,5,36,2,3,1,3),_DpmPIDMapPEID_Type())
dpmPIDMapPEID.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmPIDMapPEID.setStatus(_A)
class _DpmPIDMapRow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_DpmPIDMapRow_Type.__name__=_B
_DpmPIDMapRow_Object=MibTableColumn
dpmPIDMapRow=_DpmPIDMapRow_Object((1,3,6,1,4,1,1429,2,2,5,36,2,3,1,4),_DpmPIDMapRow_Type())
dpmPIDMapRow.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmPIDMapRow.setStatus(_A)
class _DpmPIDMapStreamType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DpmPIDMapStreamType_Type.__name__=_B
_DpmPIDMapStreamType_Object=MibTableColumn
dpmPIDMapStreamType=_DpmPIDMapStreamType_Object((1,3,6,1,4,1,1429,2,2,5,36,2,3,1,5),_DpmPIDMapStreamType_Type())
dpmPIDMapStreamType.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmPIDMapStreamType.setStatus(_A)
class _DpmPIDMapStreamCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('invl',1),('pcr',2),('vid',3),('aud',4),('subt',5),('vbi',6),('dpi',7),('mpe',8),('ttx',9),('data',10),('lsdt',11),('cdt',12),('etv',13),('ukn',14)))
_DpmPIDMapStreamCategory_Type.__name__=_B
_DpmPIDMapStreamCategory_Object=MibTableColumn
dpmPIDMapStreamCategory=_DpmPIDMapStreamCategory_Object((1,3,6,1,4,1,1429,2,2,5,36,2,3,1,6),_DpmPIDMapStreamCategory_Type())
dpmPIDMapStreamCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmPIDMapStreamCategory.setStatus(_A)
class _DpmPIDMapStreamInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_DpmPIDMapStreamInstance_Type.__name__=_B
_DpmPIDMapStreamInstance_Object=MibTableColumn
dpmPIDMapStreamInstance=_DpmPIDMapStreamInstance_Object((1,3,6,1,4,1,1429,2,2,5,36,2,3,1,7),_DpmPIDMapStreamInstance_Type())
dpmPIDMapStreamInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmPIDMapStreamInstance.setStatus(_A)
class _DpmPIDMapAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_D,1),('map',3)))
_DpmPIDMapAction_Type.__name__=_B
_DpmPIDMapAction_Object=MibTableColumn
dpmPIDMapAction=_DpmPIDMapAction_Object((1,3,6,1,4,1,1429,2,2,5,36,2,3,1,8),_DpmPIDMapAction_Type())
dpmPIDMapAction.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmPIDMapAction.setStatus(_A)
class _DpmPIDMapOutputPID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8192))
_DpmPIDMapOutputPID_Type.__name__=_B
_DpmPIDMapOutputPID_Object=MibTableColumn
dpmPIDMapOutputPID=_DpmPIDMapOutputPID_Object((1,3,6,1,4,1,1429,2,2,5,36,2,3,1,9),_DpmPIDMapOutputPID_Type())
dpmPIDMapOutputPID.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmPIDMapOutputPID.setStatus(_A)
_DpmPIDMapInuse_Type=RowStatus
_DpmPIDMapInuse_Object=MibTableColumn
dpmPIDMapInuse=_DpmPIDMapInuse_Object((1,3,6,1,4,1,1429,2,2,5,36,2,3,1,10),_DpmPIDMapInuse_Type())
dpmPIDMapInuse.setMaxAccess(_C)
if mibBuilder.loadTexts:dpmPIDMapInuse.setStatus(_A)
_DpmAlignedPMTTable_Object=MibTable
dpmAlignedPMTTable=_DpmAlignedPMTTable_Object((1,3,6,1,4,1,1429,2,2,5,36,2,4))
if mibBuilder.loadTexts:dpmAlignedPMTTable.setStatus(_A)
_DpmAlignedPMTEntry_Object=MibTableRow
dpmAlignedPMTEntry=_DpmAlignedPMTEntry_Object((1,3,6,1,4,1,1429,2,2,5,36,2,4,1))
dpmAlignedPMTEntry.setIndexNames((0,_G,_O),(0,_G,_P),(0,_G,_Q))
if mibBuilder.loadTexts:dpmAlignedPMTEntry.setStatus(_A)
class _DpmAlignedPMTInstanceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_DpmAlignedPMTInstanceID_Type.__name__=_B
_DpmAlignedPMTInstanceID_Object=MibTableColumn
dpmAlignedPMTInstanceID=_DpmAlignedPMTInstanceID_Object((1,3,6,1,4,1,1429,2,2,5,36,2,4,1,1),_DpmAlignedPMTInstanceID_Type())
dpmAlignedPMTInstanceID.setMaxAccess(_F)
if mibBuilder.loadTexts:dpmAlignedPMTInstanceID.setStatus(_A)
class _DpmAlignedPMTPEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_DpmAlignedPMTPEID_Type.__name__=_B
_DpmAlignedPMTPEID_Object=MibTableColumn
dpmAlignedPMTPEID=_DpmAlignedPMTPEID_Object((1,3,6,1,4,1,1429,2,2,5,36,2,4,1,2),_DpmAlignedPMTPEID_Type())
dpmAlignedPMTPEID.setMaxAccess(_F)
if mibBuilder.loadTexts:dpmAlignedPMTPEID.setStatus(_A)
class _DpmAlignedPMTRow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_DpmAlignedPMTRow_Type.__name__=_B
_DpmAlignedPMTRow_Object=MibTableColumn
dpmAlignedPMTRow=_DpmAlignedPMTRow_Object((1,3,6,1,4,1,1429,2,2,5,36,2,4,1,3),_DpmAlignedPMTRow_Type())
dpmAlignedPMTRow.setMaxAccess(_F)
if mibBuilder.loadTexts:dpmAlignedPMTRow.setStatus(_A)
class _DpmAlignedPMTStreamTypeTxt_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_DpmAlignedPMTStreamTypeTxt_Type.__name__=_J
_DpmAlignedPMTStreamTypeTxt_Object=MibTableColumn
dpmAlignedPMTStreamTypeTxt=_DpmAlignedPMTStreamTypeTxt_Object((1,3,6,1,4,1,1429,2,2,5,36,2,4,1,4),_DpmAlignedPMTStreamTypeTxt_Type())
dpmAlignedPMTStreamTypeTxt.setMaxAccess(_F)
if mibBuilder.loadTexts:dpmAlignedPMTStreamTypeTxt.setStatus(_A)
class _DpmAlignedPMTInputPID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8192))
_DpmAlignedPMTInputPID_Type.__name__=_B
_DpmAlignedPMTInputPID_Object=MibTableColumn
dpmAlignedPMTInputPID=_DpmAlignedPMTInputPID_Object((1,3,6,1,4,1,1429,2,2,5,36,2,4,1,5),_DpmAlignedPMTInputPID_Type())
dpmAlignedPMTInputPID.setMaxAccess(_F)
if mibBuilder.loadTexts:dpmAlignedPMTInputPID.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'ciscoDSGDPM':ciscoDSGDPM,'dpmInfo':dpmInfo,'dpmRegenerate':dpmRegenerate,'dpmTable':dpmTable,'dpmGblCfgTable':dpmGblCfgTable,'dpmGblCfgEntry':dpmGblCfgEntry,_K:dpmGblCfgInstanceID,'dpmGblCfgInstanceName':dpmGblCfgInstanceName,'dpmGblCfgMapMode':dpmGblCfgMapMode,'dpmGblCfgDupMethod':dpmGblCfgDupMethod,'dpmGblCfgRegenRate':dpmGblCfgRegenRate,'dpmGblCfgUnrefContent':dpmGblCfgUnrefContent,'dpmGblCfgPSIOutput':dpmGblCfgPSIOutput,'dpmGblCfgSVCIDOutput':dpmGblCfgSVCIDOutput,'dpmGblCfgPSIPAT':dpmGblCfgPSIPAT,'dpmGblCfgPSICAT':dpmGblCfgPSICAT,'dpmGblCfgPSIPMT':dpmGblCfgPSIPMT,'dpmGblCfgPSITSDT':dpmGblCfgPSITSDT,'dpmGblCfgPSINIT':dpmGblCfgPSINIT,'dpmGblCfgPSINITO':dpmGblCfgPSINITO,'dpmGblCfgPSISDT':dpmGblCfgPSISDT,'dpmGblCfgPSISDTO':dpmGblCfgPSISDTO,'dpmGblCfgPSIBAT':dpmGblCfgPSIBAT,'dpmGblCfgPSIEIT':dpmGblCfgPSIEIT,'dpmGblCfgPSITDT':dpmGblCfgPSITDT,'dpmGblCfgPSIST':dpmGblCfgPSIST,'dpmGblCfgPSIRST':dpmGblCfgPSIRST,'dpmGblCfgPSITOT':dpmGblCfgPSITOT,'dpmGblCfgPSIDIT':dpmGblCfgPSIDIT,'dpmGblCfgPSISIT':dpmGblCfgPSISIT,'dpmGblCfgPSIECM':dpmGblCfgPSIECM,'dpmGblCfgPSIEMM':dpmGblCfgPSIEMM,'dpmGblCfgPSIDRT':dpmGblCfgPSIDRT,'dpmGblCfgPSICDT':dpmGblCfgPSICDT,'dpmGblCfgPATPMTOffset':dpmGblCfgPATPMTOffset,'dpmGblCfgNITOffset':dpmGblCfgNITOffset,'dpmPeMappingTable':dpmPeMappingTable,'dpmPeMappingEntry':dpmPeMappingEntry,_L:dpmPeMappingInstanceID,_M:dpmPeMappingPEID,'dpmPeMappingAction':dpmPeMappingAction,'dpmPeMappingPMTPID':dpmPeMappingPMTPID,'dpmPeMappingOpChannel':dpmPeMappingOpChannel,'dpmPIDMapTable':dpmPIDMapTable,'dpmPIDMapEntry':dpmPIDMapEntry,_N:dpmPIDMapIndex,'dpmPIDMapInstanceID':dpmPIDMapInstanceID,'dpmPIDMapPEID':dpmPIDMapPEID,'dpmPIDMapRow':dpmPIDMapRow,'dpmPIDMapStreamType':dpmPIDMapStreamType,'dpmPIDMapStreamCategory':dpmPIDMapStreamCategory,'dpmPIDMapStreamInstance':dpmPIDMapStreamInstance,'dpmPIDMapAction':dpmPIDMapAction,'dpmPIDMapOutputPID':dpmPIDMapOutputPID,'dpmPIDMapInuse':dpmPIDMapInuse,'dpmAlignedPMTTable':dpmAlignedPMTTable,'dpmAlignedPMTEntry':dpmAlignedPMTEntry,_O:dpmAlignedPMTInstanceID,_P:dpmAlignedPMTPEID,_Q:dpmAlignedPMTRow,'dpmAlignedPMTStreamTypeTxt':dpmAlignedPMTStreamTypeTxt,'dpmAlignedPMTInputPID':dpmAlignedPMTInputPID})