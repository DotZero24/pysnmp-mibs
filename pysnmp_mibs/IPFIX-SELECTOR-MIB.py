_D='ipfixSelectorBasicGroup'
_C='ipfixFuncSelectAllAvail'
_B='IPFIX-SELECTOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ipfixSelectorMIB=ModuleIdentity((1,3,6,1,2,1,194))
if mibBuilder.loadTexts:ipfixSelectorMIB.setRevisions(('2012-06-11 00:00','2010-03-15 00:00'))
_IpfixSelectorObjects_ObjectIdentity=ObjectIdentity
ipfixSelectorObjects=_IpfixSelectorObjects_ObjectIdentity((1,3,6,1,2,1,194,1))
_IpfixSelectorFunctions_ObjectIdentity=ObjectIdentity
ipfixSelectorFunctions=_IpfixSelectorFunctions_ObjectIdentity((1,3,6,1,2,1,194,1,1))
_IpfixFuncSelectAll_ObjectIdentity=ObjectIdentity
ipfixFuncSelectAll=_IpfixFuncSelectAll_ObjectIdentity((1,3,6,1,2,1,194,1,1,1))
_IpfixFuncSelectAllAvail_Type=TruthValue
_IpfixFuncSelectAllAvail_Object=MibScalar
ipfixFuncSelectAllAvail=_IpfixFuncSelectAllAvail_Object((1,3,6,1,2,1,194,1,1,1,1),_IpfixFuncSelectAllAvail_Type())
ipfixFuncSelectAllAvail.setMaxAccess('read-only')
if mibBuilder.loadTexts:ipfixFuncSelectAllAvail.setStatus(_A)
_IpfixSelectorConformance_ObjectIdentity=ObjectIdentity
ipfixSelectorConformance=_IpfixSelectorConformance_ObjectIdentity((1,3,6,1,2,1,194,2))
_IpfixSelectorCompliances_ObjectIdentity=ObjectIdentity
ipfixSelectorCompliances=_IpfixSelectorCompliances_ObjectIdentity((1,3,6,1,2,1,194,2,1))
_IpfixSelectorGroups_ObjectIdentity=ObjectIdentity
ipfixSelectorGroups=_IpfixSelectorGroups_ObjectIdentity((1,3,6,1,2,1,194,2,2))
ipfixSelectorBasicGroup=ObjectGroup((1,3,6,1,2,1,194,2,2,1))
ipfixSelectorBasicGroup.setObjects((_B,_C))
if mibBuilder.loadTexts:ipfixSelectorBasicGroup.setStatus(_A)
ipfixSelectorBasicCompliance=ModuleCompliance((1,3,6,1,2,1,194,2,1,1))
ipfixSelectorBasicCompliance.setObjects((_B,_D))
if mibBuilder.loadTexts:ipfixSelectorBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ipfixSelectorMIB':ipfixSelectorMIB,'ipfixSelectorObjects':ipfixSelectorObjects,'ipfixSelectorFunctions':ipfixSelectorFunctions,'ipfixFuncSelectAll':ipfixFuncSelectAll,_C:ipfixFuncSelectAllAvail,'ipfixSelectorConformance':ipfixSelectorConformance,'ipfixSelectorCompliances':ipfixSelectorCompliances,'ipfixSelectorBasicCompliance':ipfixSelectorBasicCompliance,'ipfixSelectorGroups':ipfixSelectorGroups,_D:ipfixSelectorBasicGroup})