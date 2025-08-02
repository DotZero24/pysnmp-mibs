_J='dcxCMMTrapReason'
_I='dcxCMMCmtsCmStatusEntry'
_H='dcxCMMFlapMacAddr'
_G='dcxCMMCmIp'
_F='DisplayString'
_E='read-write'
_D='Integer32'
_C='ARRIS-C3-CMM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cmtsC3,=mibBuilder.importSymbols('ARRIS-MIB','cmtsC3')
TenthdBmV,docsIfCmtsCmStatusDocsisRegMode,docsIfCmtsCmStatusEntry,docsIfCmtsCmStatusIpAddress,docsIfCmtsCmStatusMacAddress=mibBuilder.importSymbols('DOCS-IF-MIB','TenthdBmV','docsIfCmtsCmStatusDocsisRegMode','docsIfCmtsCmStatusEntry','docsIfCmtsCmStatusIpAddress','docsIfCmtsCmStatusMacAddress')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'MacAddress','PhysAddress','TextualConvention','TruthValue')
cmtsC3CMMMIB=ModuleIdentity((1,3,6,1,4,1,4115,1,4,3,5))
if mibBuilder.loadTexts:cmtsC3CMMMIB.setRevisions(('2005-02-02 00:00',))
_DcxCMMObjects_ObjectIdentity=ObjectIdentity
dcxCMMObjects=_DcxCMMObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,4,3,5,1))
_DcxCMMCmtsCmStatusTable_Object=MibTable
dcxCMMCmtsCmStatusTable=_DcxCMMCmtsCmStatusTable_Object((1,3,6,1,4,1,4115,1,4,3,5,1,1))
if mibBuilder.loadTexts:dcxCMMCmtsCmStatusTable.setStatus(_A)
_DcxCMMCmtsCmStatusEntry_Object=MibTableRow
dcxCMMCmtsCmStatusEntry=_DcxCMMCmtsCmStatusEntry_Object((1,3,6,1,4,1,4115,1,4,3,5,1,1,1))
if mibBuilder.loadTexts:dcxCMMCmtsCmStatusEntry.setStatus(_A)
_DcxCMMCmDebugLevel_Type=Unsigned32
_DcxCMMCmDebugLevel_Object=MibTableColumn
dcxCMMCmDebugLevel=_DcxCMMCmDebugLevel_Object((1,3,6,1,4,1,4115,1,4,3,5,1,1,1,1),_DcxCMMCmDebugLevel_Type())
dcxCMMCmDebugLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:dcxCMMCmDebugLevel.setStatus(_A)
_DcxCMMUpDisable_Type=Unsigned32
_DcxCMMUpDisable_Object=MibTableColumn
dcxCMMUpDisable=_DcxCMMUpDisable_Object((1,3,6,1,4,1,4115,1,4,3,5,1,1,1,2),_DcxCMMUpDisable_Type())
dcxCMMUpDisable.setMaxAccess(_E)
if mibBuilder.loadTexts:dcxCMMUpDisable.setStatus(_A)
class _DcxCMMResetCm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('reset',1),('delete',2),('none',3)))
_DcxCMMResetCm_Type.__name__=_D
_DcxCMMResetCm_Object=MibTableColumn
dcxCMMResetCm=_DcxCMMResetCm_Object((1,3,6,1,4,1,4115,1,4,3,5,1,1,1,3),_DcxCMMResetCm_Type())
dcxCMMResetCm.setMaxAccess(_E)
if mibBuilder.loadTexts:dcxCMMResetCm.setStatus(_A)
_DcxCMMResetCounters_Type=TruthValue
_DcxCMMResetCounters_Object=MibTableColumn
dcxCMMResetCounters=_DcxCMMResetCounters_Object((1,3,6,1,4,1,4115,1,4,3,5,1,1,1,4),_DcxCMMResetCounters_Type())
dcxCMMResetCounters.setMaxAccess(_E)
if mibBuilder.loadTexts:dcxCMMResetCounters.setStatus(_A)
class _DcxCMMCmBpiState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('cmBPI2NotManagedByBPI2',0),('cmBPI2InBPI2Progress',1),('cmBPI2NotAuthorized',2),('cmBPI2KeyIssued',3),('cmBPI2IsRunning',4)))
_DcxCMMCmBpiState_Type.__name__=_D
_DcxCMMCmBpiState_Object=MibTableColumn
dcxCMMCmBpiState=_DcxCMMCmBpiState_Object((1,3,6,1,4,1,4115,1,4,3,5,1,1,1,5),_DcxCMMCmBpiState_Type())
dcxCMMCmBpiState.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxCMMCmBpiState.setStatus(_A)
_DcxCMMCmPrimaryUsSf_Type=Unsigned32
_DcxCMMCmPrimaryUsSf_Object=MibTableColumn
dcxCMMCmPrimaryUsSf=_DcxCMMCmPrimaryUsSf_Object((1,3,6,1,4,1,4115,1,4,3,5,1,1,1,6),_DcxCMMCmPrimaryUsSf_Type())
dcxCMMCmPrimaryUsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxCMMCmPrimaryUsSf.setStatus(_A)
_DcxCMMCmPrimaryDsSf_Type=Unsigned32
_DcxCMMCmPrimaryDsSf_Object=MibTableColumn
dcxCMMCmPrimaryDsSf=_DcxCMMCmPrimaryDsSf_Object((1,3,6,1,4,1,4115,1,4,3,5,1,1,1,7),_DcxCMMCmPrimaryDsSf_Type())
dcxCMMCmPrimaryDsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxCMMCmPrimaryDsSf.setStatus(_A)
_DcxCMMIpToCmTable_Object=MibTable
dcxCMMIpToCmTable=_DcxCMMIpToCmTable_Object((1,3,6,1,4,1,4115,1,4,3,5,1,2))
if mibBuilder.loadTexts:dcxCMMIpToCmTable.setStatus(_A)
_DcxCMMIpToCmEntry_Object=MibTableRow
dcxCMMIpToCmEntry=_DcxCMMIpToCmEntry_Object((1,3,6,1,4,1,4115,1,4,3,5,1,2,1))
dcxCMMIpToCmEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:dcxCMMIpToCmEntry.setStatus(_A)
_DcxCMMCmIp_Type=IpAddress
_DcxCMMCmIp_Object=MibTableColumn
dcxCMMCmIp=_DcxCMMCmIp_Object((1,3,6,1,4,1,4115,1,4,3,5,1,2,1,1),_DcxCMMCmIp_Type())
dcxCMMCmIp.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dcxCMMCmIp.setStatus(_A)
class _DcxCMMCmPtr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DcxCMMCmPtr_Type.__name__=_D
_DcxCMMCmPtr_Object=MibTableColumn
dcxCMMCmPtr=_DcxCMMCmPtr_Object((1,3,6,1,4,1,4115,1,4,3,5,1,2,1,2),_DcxCMMCmPtr_Type())
dcxCMMCmPtr.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxCMMCmPtr.setStatus(_A)
_DcxCMMFlapTable_Object=MibTable
dcxCMMFlapTable=_DcxCMMFlapTable_Object((1,3,6,1,4,1,4115,1,4,3,5,1,3))
if mibBuilder.loadTexts:dcxCMMFlapTable.setStatus(_A)
_DcxCMMCmFlapEntry_Object=MibTableRow
dcxCMMCmFlapEntry=_DcxCMMCmFlapEntry_Object((1,3,6,1,4,1,4115,1,4,3,5,1,3,1))
dcxCMMCmFlapEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:dcxCMMCmFlapEntry.setStatus(_A)
_DcxCMMFlapMacAddr_Type=MacAddress
_DcxCMMFlapMacAddr_Object=MibTableColumn
dcxCMMFlapMacAddr=_DcxCMMFlapMacAddr_Object((1,3,6,1,4,1,4115,1,4,3,5,1,3,1,2),_DcxCMMFlapMacAddr_Type())
dcxCMMFlapMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxCMMFlapMacAddr.setStatus(_A)
_DcxCMMFlapUpstreamID_Type=Unsigned32
_DcxCMMFlapUpstreamID_Object=MibTableColumn
dcxCMMFlapUpstreamID=_DcxCMMFlapUpstreamID_Object((1,3,6,1,4,1,4115,1,4,3,5,1,3,1,3),_DcxCMMFlapUpstreamID_Type())
dcxCMMFlapUpstreamID.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxCMMFlapUpstreamID.setStatus(_A)
_DcxCMMFlapInsertions_Type=Unsigned32
_DcxCMMFlapInsertions_Object=MibTableColumn
dcxCMMFlapInsertions=_DcxCMMFlapInsertions_Object((1,3,6,1,4,1,4115,1,4,3,5,1,3,1,4),_DcxCMMFlapInsertions_Type())
dcxCMMFlapInsertions.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxCMMFlapInsertions.setStatus(_A)
_DcxCMMFlapHits_Type=Unsigned32
_DcxCMMFlapHits_Object=MibTableColumn
dcxCMMFlapHits=_DcxCMMFlapHits_Object((1,3,6,1,4,1,4115,1,4,3,5,1,3,1,5),_DcxCMMFlapHits_Type())
dcxCMMFlapHits.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxCMMFlapHits.setStatus(_A)
_DcxCMMFlapMisses_Type=Unsigned32
_DcxCMMFlapMisses_Object=MibTableColumn
dcxCMMFlapMisses=_DcxCMMFlapMisses_Object((1,3,6,1,4,1,4115,1,4,3,5,1,3,1,6),_DcxCMMFlapMisses_Type())
dcxCMMFlapMisses.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxCMMFlapMisses.setStatus(_A)
_DcxCMMFlapCRC_Type=Unsigned32
_DcxCMMFlapCRC_Object=MibTableColumn
dcxCMMFlapCRC=_DcxCMMFlapCRC_Object((1,3,6,1,4,1,4115,1,4,3,5,1,3,1,7),_DcxCMMFlapCRC_Type())
dcxCMMFlapCRC.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxCMMFlapCRC.setStatus(_A)
_DcxCMMFlapCount_Type=Unsigned32
_DcxCMMFlapCount_Object=MibTableColumn
dcxCMMFlapCount=_DcxCMMFlapCount_Object((1,3,6,1,4,1,4115,1,4,3,5,1,3,1,9),_DcxCMMFlapCount_Type())
dcxCMMFlapCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxCMMFlapCount.setStatus(_A)
_DcxCMMFlapTimeStamp_Type=Unsigned32
_DcxCMMFlapTimeStamp_Object=MibTableColumn
dcxCMMFlapTimeStamp=_DcxCMMFlapTimeStamp_Object((1,3,6,1,4,1,4115,1,4,3,5,1,3,1,10),_DcxCMMFlapTimeStamp_Type())
dcxCMMFlapTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxCMMFlapTimeStamp.setStatus(_A)
_DcxCMMTrapGroup_ObjectIdentity=ObjectIdentity
dcxCMMTrapGroup=_DcxCMMTrapGroup_ObjectIdentity((1,3,6,1,4,1,4115,1,4,3,5,1,4))
class _DcxCMMTrapReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcxCMMTrapReason_Type.__name__=_F
_DcxCMMTrapReason_Object=MibScalar
dcxCMMTrapReason=_DcxCMMTrapReason_Object((1,3,6,1,4,1,4115,1,4,3,5,1,4,1),_DcxCMMTrapReason_Type())
dcxCMMTrapReason.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:dcxCMMTrapReason.setStatus(_A)
docsIfCmtsCmStatusEntry.registerAugmentions((_C,_I))
dcxCMMCmtsCmStatusEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())
dcxCMMTrap=NotificationType((1,3,6,1,4,1,4115,1,4,3,5,1,4,2))
dcxCMMTrap.setObjects((_C,_J))
if mibBuilder.loadTexts:dcxCMMTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cmtsC3CMMMIB':cmtsC3CMMMIB,'dcxCMMObjects':dcxCMMObjects,'dcxCMMCmtsCmStatusTable':dcxCMMCmtsCmStatusTable,_I:dcxCMMCmtsCmStatusEntry,'dcxCMMCmDebugLevel':dcxCMMCmDebugLevel,'dcxCMMUpDisable':dcxCMMUpDisable,'dcxCMMResetCm':dcxCMMResetCm,'dcxCMMResetCounters':dcxCMMResetCounters,'dcxCMMCmBpiState':dcxCMMCmBpiState,'dcxCMMCmPrimaryUsSf':dcxCMMCmPrimaryUsSf,'dcxCMMCmPrimaryDsSf':dcxCMMCmPrimaryDsSf,'dcxCMMIpToCmTable':dcxCMMIpToCmTable,'dcxCMMIpToCmEntry':dcxCMMIpToCmEntry,_G:dcxCMMCmIp,'dcxCMMCmPtr':dcxCMMCmPtr,'dcxCMMFlapTable':dcxCMMFlapTable,'dcxCMMCmFlapEntry':dcxCMMCmFlapEntry,_H:dcxCMMFlapMacAddr,'dcxCMMFlapUpstreamID':dcxCMMFlapUpstreamID,'dcxCMMFlapInsertions':dcxCMMFlapInsertions,'dcxCMMFlapHits':dcxCMMFlapHits,'dcxCMMFlapMisses':dcxCMMFlapMisses,'dcxCMMFlapCRC':dcxCMMFlapCRC,'dcxCMMFlapCount':dcxCMMFlapCount,'dcxCMMFlapTimeStamp':dcxCMMFlapTimeStamp,'dcxCMMTrapGroup':dcxCMMTrapGroup,_J:dcxCMMTrapReason,'dcxCMMTrap':dcxCMMTrap})