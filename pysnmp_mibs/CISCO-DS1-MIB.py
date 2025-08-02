_J='coiDS1PMHisBucketNumber'
_I='coiDS1PMHisIntervalType'
_H='coiDS1CurrentIntervalType'
_G='Unsigned32'
_F='not-accessible'
_E='ifIndex'
_D='IF-MIB'
_C='CISCO-DS1-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,ifDescr,ifIndex=mibBuilder.importSymbols(_D,'InterfaceIndex','ifDescr',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoDs1MIB=ModuleIdentity((1,3,6,1,4,1,9,9,1055))
class CoiIntervalType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMin',1),('oneDay',2)))
_CiscoDs1MIBNotifs_ObjectIdentity=ObjectIdentity
ciscoDs1MIBNotifs=_CiscoDs1MIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,1055,0))
_CiscoDs1MIBObjects_ObjectIdentity=ObjectIdentity
ciscoDs1MIBObjects=_CiscoDs1MIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,1055,1))
_CiscoDS1PMData_ObjectIdentity=ObjectIdentity
ciscoDS1PMData=_CiscoDS1PMData_ObjectIdentity((1,3,6,1,4,1,9,9,1055,1,1))
_CoiDS1PMCurrentTable_Object=MibTable
coiDS1PMCurrentTable=_CoiDS1PMCurrentTable_Object((1,3,6,1,4,1,9,9,1055,1,1,1))
if mibBuilder.loadTexts:coiDS1PMCurrentTable.setStatus(_A)
_CoiDS1PMCurrentEntry_Object=MibTableRow
coiDS1PMCurrentEntry=_CoiDS1PMCurrentEntry_Object((1,3,6,1,4,1,9,9,1055,1,1,1,1))
coiDS1PMCurrentEntry.setIndexNames((0,_D,_E),(0,_C,_H))
if mibBuilder.loadTexts:coiDS1PMCurrentEntry.setStatus(_A)
_CoiDS1CurrentIntervalType_Type=CoiIntervalType
_CoiDS1CurrentIntervalType_Object=MibTableColumn
coiDS1CurrentIntervalType=_CoiDS1CurrentIntervalType_Object((1,3,6,1,4,1,9,9,1055,1,1,1,1,1),_CoiDS1CurrentIntervalType_Type())
coiDS1CurrentIntervalType.setMaxAccess(_F)
if mibBuilder.loadTexts:coiDS1CurrentIntervalType.setStatus(_A)
_CoiDS1CurrentLCVs_Type=Counter32
_CoiDS1CurrentLCVs_Object=MibTableColumn
coiDS1CurrentLCVs=_CoiDS1CurrentLCVs_Object((1,3,6,1,4,1,9,9,1055,1,1,1,1,2),_CoiDS1CurrentLCVs_Type())
coiDS1CurrentLCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1CurrentLCVs.setStatus(_A)
_CoiDS1CurrentPCVs_Type=Counter32
_CoiDS1CurrentPCVs_Object=MibTableColumn
coiDS1CurrentPCVs=_CoiDS1CurrentPCVs_Object((1,3,6,1,4,1,9,9,1055,1,1,1,1,3),_CoiDS1CurrentPCVs_Type())
coiDS1CurrentPCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1CurrentPCVs.setStatus(_A)
_CoiDS1CurrentSELSs_Type=Counter32
_CoiDS1CurrentSELSs_Object=MibTableColumn
coiDS1CurrentSELSs=_CoiDS1CurrentSELSs_Object((1,3,6,1,4,1,9,9,1055,1,1,1,1,4),_CoiDS1CurrentSELSs_Type())
coiDS1CurrentSELSs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1CurrentSELSs.setStatus(_A)
_CoiDS1CurrentLESs_Type=Counter32
_CoiDS1CurrentLESs_Object=MibTableColumn
coiDS1CurrentLESs=_CoiDS1CurrentLESs_Object((1,3,6,1,4,1,9,9,1055,1,1,1,1,5),_CoiDS1CurrentLESs_Type())
coiDS1CurrentLESs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1CurrentLESs.setStatus(_A)
_CoiDS1CurrentAISs_Type=Counter32
_CoiDS1CurrentAISs_Object=MibTableColumn
coiDS1CurrentAISs=_CoiDS1CurrentAISs_Object((1,3,6,1,4,1,9,9,1055,1,1,1,1,6),_CoiDS1CurrentAISs_Type())
coiDS1CurrentAISs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1CurrentAISs.setStatus(_A)
_CoiDS1CurrentFCPs_Type=Counter32
_CoiDS1CurrentFCPs_Object=MibTableColumn
coiDS1CurrentFCPs=_CoiDS1CurrentFCPs_Object((1,3,6,1,4,1,9,9,1055,1,1,1,1,7),_CoiDS1CurrentFCPs_Type())
coiDS1CurrentFCPs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1CurrentFCPs.setStatus(_A)
_CoiDS1CurrentESs_Type=Counter32
_CoiDS1CurrentESs_Object=MibTableColumn
coiDS1CurrentESs=_CoiDS1CurrentESs_Object((1,3,6,1,4,1,9,9,1055,1,1,1,1,8),_CoiDS1CurrentESs_Type())
coiDS1CurrentESs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1CurrentESs.setStatus(_A)
_CoiDS1CurrentSESs_Type=Counter32
_CoiDS1CurrentSESs_Object=MibTableColumn
coiDS1CurrentSESs=_CoiDS1CurrentSESs_Object((1,3,6,1,4,1,9,9,1055,1,1,1,1,9),_CoiDS1CurrentSESs_Type())
coiDS1CurrentSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1CurrentSESs.setStatus(_A)
_CoiDS1CurrentUASs_Type=Counter32
_CoiDS1CurrentUASs_Object=MibTableColumn
coiDS1CurrentUASs=_CoiDS1CurrentUASs_Object((1,3,6,1,4,1,9,9,1055,1,1,1,1,10),_CoiDS1CurrentUASs_Type())
coiDS1CurrentUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1CurrentUASs.setStatus(_A)
_CoiDS1CurrentESFEs_Type=Counter32
_CoiDS1CurrentESFEs_Object=MibTableColumn
coiDS1CurrentESFEs=_CoiDS1CurrentESFEs_Object((1,3,6,1,4,1,9,9,1055,1,1,1,1,11),_CoiDS1CurrentESFEs_Type())
coiDS1CurrentESFEs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1CurrentESFEs.setStatus(_A)
_CoiDS1CurrentSESFEs_Type=Counter32
_CoiDS1CurrentSESFEs_Object=MibTableColumn
coiDS1CurrentSESFEs=_CoiDS1CurrentSESFEs_Object((1,3,6,1,4,1,9,9,1055,1,1,1,1,12),_CoiDS1CurrentSESFEs_Type())
coiDS1CurrentSESFEs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1CurrentSESFEs.setStatus(_A)
_CoiDS1CurrentUASFEs_Type=Counter32
_CoiDS1CurrentUASFEs_Object=MibTableColumn
coiDS1CurrentUASFEs=_CoiDS1CurrentUASFEs_Object((1,3,6,1,4,1,9,9,1055,1,1,1,1,13),_CoiDS1CurrentUASFEs_Type())
coiDS1CurrentUASFEs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1CurrentUASFEs.setStatus(_A)
_CoiDS1currentPMValidData_Type=TruthValue
_CoiDS1currentPMValidData_Object=MibTableColumn
coiDS1currentPMValidData=_CoiDS1currentPMValidData_Object((1,3,6,1,4,1,9,9,1055,1,1,1,1,14),_CoiDS1currentPMValidData_Type())
coiDS1currentPMValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1currentPMValidData.setStatus(_A)
_CoiDS1PMHisTable_Object=MibTable
coiDS1PMHisTable=_CoiDS1PMHisTable_Object((1,3,6,1,4,1,9,9,1055,1,1,2))
if mibBuilder.loadTexts:coiDS1PMHisTable.setStatus(_A)
_CoiDS1PMHisEntry_Object=MibTableRow
coiDS1PMHisEntry=_CoiDS1PMHisEntry_Object((1,3,6,1,4,1,9,9,1055,1,1,2,1))
coiDS1PMHisEntry.setIndexNames((0,_D,_E),(0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:coiDS1PMHisEntry.setStatus(_A)
_CoiDS1PMHisIntervalType_Type=CoiIntervalType
_CoiDS1PMHisIntervalType_Object=MibTableColumn
coiDS1PMHisIntervalType=_CoiDS1PMHisIntervalType_Object((1,3,6,1,4,1,9,9,1055,1,1,2,1,1),_CoiDS1PMHisIntervalType_Type())
coiDS1PMHisIntervalType.setMaxAccess(_F)
if mibBuilder.loadTexts:coiDS1PMHisIntervalType.setStatus(_A)
class _CoiDS1PMHisBucketNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CoiDS1PMHisBucketNumber_Type.__name__=_G
_CoiDS1PMHisBucketNumber_Object=MibTableColumn
coiDS1PMHisBucketNumber=_CoiDS1PMHisBucketNumber_Object((1,3,6,1,4,1,9,9,1055,1,1,2,1,2),_CoiDS1PMHisBucketNumber_Type())
coiDS1PMHisBucketNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:coiDS1PMHisBucketNumber.setStatus(_A)
_CoiDS1HisLCVs_Type=Counter32
_CoiDS1HisLCVs_Object=MibTableColumn
coiDS1HisLCVs=_CoiDS1HisLCVs_Object((1,3,6,1,4,1,9,9,1055,1,1,2,1,3),_CoiDS1HisLCVs_Type())
coiDS1HisLCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1HisLCVs.setStatus(_A)
_CoiDS1HisPCVs_Type=Counter32
_CoiDS1HisPCVs_Object=MibTableColumn
coiDS1HisPCVs=_CoiDS1HisPCVs_Object((1,3,6,1,4,1,9,9,1055,1,1,2,1,4),_CoiDS1HisPCVs_Type())
coiDS1HisPCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1HisPCVs.setStatus(_A)
_CoiDS1HisSELSs_Type=Counter32
_CoiDS1HisSELSs_Object=MibTableColumn
coiDS1HisSELSs=_CoiDS1HisSELSs_Object((1,3,6,1,4,1,9,9,1055,1,1,2,1,5),_CoiDS1HisSELSs_Type())
coiDS1HisSELSs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1HisSELSs.setStatus(_A)
_CoiDS1HisLESs_Type=Counter32
_CoiDS1HisLESs_Object=MibTableColumn
coiDS1HisLESs=_CoiDS1HisLESs_Object((1,3,6,1,4,1,9,9,1055,1,1,2,1,6),_CoiDS1HisLESs_Type())
coiDS1HisLESs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1HisLESs.setStatus(_A)
_CoiDS1HisAISs_Type=Counter32
_CoiDS1HisAISs_Object=MibTableColumn
coiDS1HisAISs=_CoiDS1HisAISs_Object((1,3,6,1,4,1,9,9,1055,1,1,2,1,7),_CoiDS1HisAISs_Type())
coiDS1HisAISs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1HisAISs.setStatus(_A)
_CoiDS1HisFCPs_Type=Counter32
_CoiDS1HisFCPs_Object=MibTableColumn
coiDS1HisFCPs=_CoiDS1HisFCPs_Object((1,3,6,1,4,1,9,9,1055,1,1,2,1,8),_CoiDS1HisFCPs_Type())
coiDS1HisFCPs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1HisFCPs.setStatus(_A)
_CoiDS1HisESs_Type=Counter32
_CoiDS1HisESs_Object=MibTableColumn
coiDS1HisESs=_CoiDS1HisESs_Object((1,3,6,1,4,1,9,9,1055,1,1,2,1,9),_CoiDS1HisESs_Type())
coiDS1HisESs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1HisESs.setStatus(_A)
_CoiDS1HisSESs_Type=Counter32
_CoiDS1HisSESs_Object=MibTableColumn
coiDS1HisSESs=_CoiDS1HisSESs_Object((1,3,6,1,4,1,9,9,1055,1,1,2,1,10),_CoiDS1HisSESs_Type())
coiDS1HisSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1HisSESs.setStatus(_A)
_CoiDS1HisUASs_Type=Counter32
_CoiDS1HisUASs_Object=MibTableColumn
coiDS1HisUASs=_CoiDS1HisUASs_Object((1,3,6,1,4,1,9,9,1055,1,1,2,1,11),_CoiDS1HisUASs_Type())
coiDS1HisUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1HisUASs.setStatus(_A)
_CoiDS1HisESFEs_Type=Counter32
_CoiDS1HisESFEs_Object=MibTableColumn
coiDS1HisESFEs=_CoiDS1HisESFEs_Object((1,3,6,1,4,1,9,9,1055,1,1,2,1,12),_CoiDS1HisESFEs_Type())
coiDS1HisESFEs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1HisESFEs.setStatus(_A)
_CoiDS1HisSESFEs_Type=Counter32
_CoiDS1HisSESFEs_Object=MibTableColumn
coiDS1HisSESFEs=_CoiDS1HisSESFEs_Object((1,3,6,1,4,1,9,9,1055,1,1,2,1,13),_CoiDS1HisSESFEs_Type())
coiDS1HisSESFEs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1HisSESFEs.setStatus(_A)
_CoiDS1HisUASFEs_Type=Counter32
_CoiDS1HisUASFEs_Object=MibTableColumn
coiDS1HisUASFEs=_CoiDS1HisUASFEs_Object((1,3,6,1,4,1,9,9,1055,1,1,2,1,14),_CoiDS1HisUASFEs_Type())
coiDS1HisUASFEs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1HisUASFEs.setStatus(_A)
_CoiDS1HisPMValidData_Type=TruthValue
_CoiDS1HisPMValidData_Object=MibTableColumn
coiDS1HisPMValidData=_CoiDS1HisPMValidData_Object((1,3,6,1,4,1,9,9,1055,1,1,2,1,15),_CoiDS1HisPMValidData_Type())
coiDS1HisPMValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:coiDS1HisPMValidData.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'CoiIntervalType':CoiIntervalType,'ciscoDs1MIB':ciscoDs1MIB,'ciscoDs1MIBNotifs':ciscoDs1MIBNotifs,'ciscoDs1MIBObjects':ciscoDs1MIBObjects,'ciscoDS1PMData':ciscoDS1PMData,'coiDS1PMCurrentTable':coiDS1PMCurrentTable,'coiDS1PMCurrentEntry':coiDS1PMCurrentEntry,_H:coiDS1CurrentIntervalType,'coiDS1CurrentLCVs':coiDS1CurrentLCVs,'coiDS1CurrentPCVs':coiDS1CurrentPCVs,'coiDS1CurrentSELSs':coiDS1CurrentSELSs,'coiDS1CurrentLESs':coiDS1CurrentLESs,'coiDS1CurrentAISs':coiDS1CurrentAISs,'coiDS1CurrentFCPs':coiDS1CurrentFCPs,'coiDS1CurrentESs':coiDS1CurrentESs,'coiDS1CurrentSESs':coiDS1CurrentSESs,'coiDS1CurrentUASs':coiDS1CurrentUASs,'coiDS1CurrentESFEs':coiDS1CurrentESFEs,'coiDS1CurrentSESFEs':coiDS1CurrentSESFEs,'coiDS1CurrentUASFEs':coiDS1CurrentUASFEs,'coiDS1currentPMValidData':coiDS1currentPMValidData,'coiDS1PMHisTable':coiDS1PMHisTable,'coiDS1PMHisEntry':coiDS1PMHisEntry,_I:coiDS1PMHisIntervalType,_J:coiDS1PMHisBucketNumber,'coiDS1HisLCVs':coiDS1HisLCVs,'coiDS1HisPCVs':coiDS1HisPCVs,'coiDS1HisSELSs':coiDS1HisSELSs,'coiDS1HisLESs':coiDS1HisLESs,'coiDS1HisAISs':coiDS1HisAISs,'coiDS1HisFCPs':coiDS1HisFCPs,'coiDS1HisESs':coiDS1HisESs,'coiDS1HisSESs':coiDS1HisSESs,'coiDS1HisUASs':coiDS1HisUASs,'coiDS1HisESFEs':coiDS1HisESFEs,'coiDS1HisSESFEs':coiDS1HisSESFEs,'coiDS1HisUASFEs':coiDS1HisUASFEs,'coiDS1HisPMValidData':coiDS1HisPMValidData})