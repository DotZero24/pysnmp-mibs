_D='eltMesIssLaAlgorithmIdx'
_C='ELTEX-MES-ISS-LA-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
eltMesIssLaMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,23))
if mibBuilder.loadTexts:eltMesIssLaMIB.setRevisions(('2020-12-28 00:00',))
_EltMesIssLaObjects_ObjectIdentity=ObjectIdentity
eltMesIssLaObjects=_EltMesIssLaObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,23,1))
_EltMesIssLaGlobals_ObjectIdentity=ObjectIdentity
eltMesIssLaGlobals=_EltMesIssLaGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,139,23,1,1))
_EltMesIssLaSelectionPolicyTable_Object=MibTable
eltMesIssLaSelectionPolicyTable=_EltMesIssLaSelectionPolicyTable_Object((1,3,6,1,4,1,35265,1,139,23,1,1,1))
if mibBuilder.loadTexts:eltMesIssLaSelectionPolicyTable.setStatus(_A)
_EltMesIssLaSelectionPolicyEntry_Object=MibTableRow
eltMesIssLaSelectionPolicyEntry=_EltMesIssLaSelectionPolicyEntry_Object((1,3,6,1,4,1,35265,1,139,23,1,1,1,1))
eltMesIssLaSelectionPolicyEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:eltMesIssLaSelectionPolicyEntry.setStatus(_A)
_EltMesIssLaAlgorithmIdx_Type=Integer32
_EltMesIssLaAlgorithmIdx_Object=MibTableColumn
eltMesIssLaAlgorithmIdx=_EltMesIssLaAlgorithmIdx_Object((1,3,6,1,4,1,35265,1,139,23,1,1,1,1,1),_EltMesIssLaAlgorithmIdx_Type())
eltMesIssLaAlgorithmIdx.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:eltMesIssLaAlgorithmIdx.setStatus(_A)
class _EltMesIssLaPortChannelSelectionPolicy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('macSrc',1),('macDst',2),('macSrcDst',3),('ipSrc',4),('ipDst',5),('ipSrcDst',6),('macIpSrcDst',7),('macIpPortSrcDst',8)))
_EltMesIssLaPortChannelSelectionPolicy_Type.__name__=_B
_EltMesIssLaPortChannelSelectionPolicy_Object=MibTableColumn
eltMesIssLaPortChannelSelectionPolicy=_EltMesIssLaPortChannelSelectionPolicy_Object((1,3,6,1,4,1,35265,1,139,23,1,1,1,1,2),_EltMesIssLaPortChannelSelectionPolicy_Type())
eltMesIssLaPortChannelSelectionPolicy.setMaxAccess('read-write')
if mibBuilder.loadTexts:eltMesIssLaPortChannelSelectionPolicy.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'eltMesIssLaMIB':eltMesIssLaMIB,'eltMesIssLaObjects':eltMesIssLaObjects,'eltMesIssLaGlobals':eltMesIssLaGlobals,'eltMesIssLaSelectionPolicyTable':eltMesIssLaSelectionPolicyTable,'eltMesIssLaSelectionPolicyEntry':eltMesIssLaSelectionPolicyEntry,_D:eltMesIssLaAlgorithmIdx,'eltMesIssLaPortChannelSelectionPolicy':eltMesIssLaPortChannelSelectionPolicy})