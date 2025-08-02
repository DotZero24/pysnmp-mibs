_G='read-create'
_F='llidIfIndex'
_E='NMS-EPON-LLID'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nmsEPONGroup,=mibBuilder.importSymbols('NMS-SMI','nmsEPONGroup')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
_NmsEponLlid_ObjectIdentity=ObjectIdentity
nmsEponLlid=_NmsEponLlid_ObjectIdentity((1,3,6,1,4,1,3320,101,9))
_NmseponllidTable_Object=MibTable
nmseponllidTable=_NmseponllidTable_Object((1,3,6,1,4,1,3320,101,9,1))
if mibBuilder.loadTexts:nmseponllidTable.setStatus(_A)
_NmsEponLlidEntry_Object=MibTableRow
nmsEponLlidEntry=_NmsEponLlidEntry_Object((1,3,6,1,4,1,3320,101,9,1,1))
nmsEponLlidEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:nmsEponLlidEntry.setStatus(_A)
_LlidIfIndex_Type=Integer32
_LlidIfIndex_Object=MibTableColumn
llidIfIndex=_LlidIfIndex_Object((1,3,6,1,4,1,3320,101,9,1,1,1),_LlidIfIndex_Type())
llidIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:llidIfIndex.setStatus(_A)
_LlidToEponPortDiid_Type=Integer32
_LlidToEponPortDiid_Object=MibTableColumn
llidToEponPortDiid=_LlidToEponPortDiid_Object((1,3,6,1,4,1,3320,101,9,1,1,2),_LlidToEponPortDiid_Type())
llidToEponPortDiid.setMaxAccess(_D)
if mibBuilder.loadTexts:llidToEponPortDiid.setStatus(_A)
_LlidsequenceNo_Type=Integer32
_LlidsequenceNo_Object=MibTableColumn
llidsequenceNo=_LlidsequenceNo_Object((1,3,6,1,4,1,3320,101,9,1,1,3),_LlidsequenceNo_Type())
llidsequenceNo.setMaxAccess(_D)
if mibBuilder.loadTexts:llidsequenceNo.setStatus(_A)
_LlidEncrypStatus_Type=TruthValue
_LlidEncrypStatus_Object=MibTableColumn
llidEncrypStatus=_LlidEncrypStatus_Object((1,3,6,1,4,1,3320,101,9,1,1,4),_LlidEncrypStatus_Type())
llidEncrypStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:llidEncrypStatus.setStatus(_A)
_LlidCtcOamExtStatus_Type=OctetString
_LlidCtcOamExtStatus_Object=MibTableColumn
llidCtcOamExtStatus=_LlidCtcOamExtStatus_Object((1,3,6,1,4,1,3320,101,9,1,1,5),_LlidCtcOamExtStatus_Type())
llidCtcOamExtStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:llidCtcOamExtStatus.setStatus(_A)
_LlidCtcOamExtOui_Type=OctetString
_LlidCtcOamExtOui_Object=MibTableColumn
llidCtcOamExtOui=_LlidCtcOamExtOui_Object((1,3,6,1,4,1,3320,101,9,1,1,6),_LlidCtcOamExtOui_Type())
llidCtcOamExtOui.setMaxAccess(_D)
if mibBuilder.loadTexts:llidCtcOamExtOui.setStatus(_A)
_LlidCtcOamExtVersion_Type=Integer32
_LlidCtcOamExtVersion_Object=MibTableColumn
llidCtcOamExtVersion=_LlidCtcOamExtVersion_Object((1,3,6,1,4,1,3320,101,9,1,1,7),_LlidCtcOamExtVersion_Type())
llidCtcOamExtVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:llidCtcOamExtVersion.setStatus(_A)
class _LlidIfPIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_LlidIfPIR_Type.__name__=_C
_LlidIfPIR_Object=MibTableColumn
llidIfPIR=_LlidIfPIR_Object((1,3,6,1,4,1,3320,101,9,1,1,8),_LlidIfPIR_Type())
llidIfPIR.setMaxAccess(_B)
if mibBuilder.loadTexts:llidIfPIR.setStatus(_A)
class _LlidIfCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,955000))
_LlidIfCIR_Type.__name__=_C
_LlidIfCIR_Object=MibTableColumn
llidIfCIR=_LlidIfCIR_Object((1,3,6,1,4,1,3320,101,9,1,1,9),_LlidIfCIR_Type())
llidIfCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:llidIfCIR.setStatus(_A)
class _LlidIfFIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,955000))
_LlidIfFIR_Type.__name__=_C
_LlidIfFIR_Object=MibTableColumn
llidIfFIR=_LlidIfFIR_Object((1,3,6,1,4,1,3320,101,9,1,1,10),_LlidIfFIR_Type())
llidIfFIR.setMaxAccess(_B)
if mibBuilder.loadTexts:llidIfFIR.setStatus(_A)
_LlidIfConfigRowStatus_Type=RowStatus
_LlidIfConfigRowStatus_Object=MibTableColumn
llidIfConfigRowStatus=_LlidIfConfigRowStatus_Object((1,3,6,1,4,1,3320,101,9,1,1,11),_LlidIfConfigRowStatus_Type())
llidIfConfigRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:llidIfConfigRowStatus.setStatus(_A)
class _LlidIfDynamicMacLearningStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_LlidIfDynamicMacLearningStatus_Type.__name__=_C
_LlidIfDynamicMacLearningStatus_Object=MibTableColumn
llidIfDynamicMacLearningStatus=_LlidIfDynamicMacLearningStatus_Object((1,3,6,1,4,1,3320,101,9,1,1,12),_LlidIfDynamicMacLearningStatus_Type())
llidIfDynamicMacLearningStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:llidIfDynamicMacLearningStatus.setStatus(_A)
_LlidIfDynamicMacLearningLimit_Type=TruthValue
_LlidIfDynamicMacLearningLimit_Object=MibTableColumn
llidIfDynamicMacLearningLimit=_LlidIfDynamicMacLearningLimit_Object((1,3,6,1,4,1,3320,101,9,1,1,13),_LlidIfDynamicMacLearningLimit_Type())
llidIfDynamicMacLearningLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:llidIfDynamicMacLearningLimit.setStatus(_A)
class _LlidIfDynamicMacLearningNumberLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1023))
_LlidIfDynamicMacLearningNumberLimit_Type.__name__=_C
_LlidIfDynamicMacLearningNumberLimit_Object=MibTableColumn
llidIfDynamicMacLearningNumberLimit=_LlidIfDynamicMacLearningNumberLimit_Object((1,3,6,1,4,1,3320,101,9,1,1,14),_LlidIfDynamicMacLearningNumberLimit_Type())
llidIfDynamicMacLearningNumberLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:llidIfDynamicMacLearningNumberLimit.setStatus(_A)
_LlidIfQosPolicy_Type=OctetString
_LlidIfQosPolicy_Object=MibTableColumn
llidIfQosPolicy=_LlidIfQosPolicy_Object((1,3,6,1,4,1,3320,101,9,1,1,15),_LlidIfQosPolicy_Type())
llidIfQosPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:llidIfQosPolicy.setStatus(_A)
_LlidIfACL_Type=OctetString
_LlidIfACL_Object=MibTableColumn
llidIfACL=_LlidIfACL_Object((1,3,6,1,4,1,3320,101,9,1,1,16),_LlidIfACL_Type())
llidIfACL.setMaxAccess(_B)
if mibBuilder.loadTexts:llidIfACL.setStatus(_A)
class _LlidDownStreamPir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_LlidDownStreamPir_Type.__name__=_C
_LlidDownStreamPir_Object=MibTableColumn
llidDownStreamPir=_LlidDownStreamPir_Object((1,3,6,1,4,1,3320,101,9,1,1,17),_LlidDownStreamPir_Type())
llidDownStreamPir.setMaxAccess(_B)
if mibBuilder.loadTexts:llidDownStreamPir.setStatus(_A)
class _LlidDownStreamCir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,955000))
_LlidDownStreamCir_Type.__name__=_C
_LlidDownStreamCir_Object=MibTableColumn
llidDownStreamCir=_LlidDownStreamCir_Object((1,3,6,1,4,1,3320,101,9,1,1,18),_LlidDownStreamCir_Type())
llidDownStreamCir.setMaxAccess(_B)
if mibBuilder.loadTexts:llidDownStreamCir.setStatus(_A)
class _LlidDownStreamFir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,955000))
_LlidDownStreamFir_Type.__name__=_C
_LlidDownStreamFir_Object=MibTableColumn
llidDownStreamFir=_LlidDownStreamFir_Object((1,3,6,1,4,1,3320,101,9,1,1,19),_LlidDownStreamFir_Type())
llidDownStreamFir.setMaxAccess(_B)
if mibBuilder.loadTexts:llidDownStreamFir.setStatus(_A)
_LlidDownStreamIfRowstatus_Type=RowStatus
_LlidDownStreamIfRowstatus_Object=MibTableColumn
llidDownStreamIfRowstatus=_LlidDownStreamIfRowstatus_Object((1,3,6,1,4,1,3320,101,9,1,1,20),_LlidDownStreamIfRowstatus_Type())
llidDownStreamIfRowstatus.setMaxAccess(_G)
if mibBuilder.loadTexts:llidDownStreamIfRowstatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'nmsEponLlid':nmsEponLlid,'nmseponllidTable':nmseponllidTable,'nmsEponLlidEntry':nmsEponLlidEntry,_F:llidIfIndex,'llidToEponPortDiid':llidToEponPortDiid,'llidsequenceNo':llidsequenceNo,'llidEncrypStatus':llidEncrypStatus,'llidCtcOamExtStatus':llidCtcOamExtStatus,'llidCtcOamExtOui':llidCtcOamExtOui,'llidCtcOamExtVersion':llidCtcOamExtVersion,'llidIfPIR':llidIfPIR,'llidIfCIR':llidIfCIR,'llidIfFIR':llidIfFIR,'llidIfConfigRowStatus':llidIfConfigRowStatus,'llidIfDynamicMacLearningStatus':llidIfDynamicMacLearningStatus,'llidIfDynamicMacLearningLimit':llidIfDynamicMacLearningLimit,'llidIfDynamicMacLearningNumberLimit':llidIfDynamicMacLearningNumberLimit,'llidIfQosPolicy':llidIfQosPolicy,'llidIfACL':llidIfACL,'llidDownStreamPir':llidDownStreamPir,'llidDownStreamCir':llidDownStreamCir,'llidDownStreamFir':llidDownStreamFir,'llidDownStreamIfRowstatus':llidDownStreamIfRowstatus})