_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
eltMesIssSnmp3MIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,19))
if mibBuilder.loadTexts:eltMesIssSnmp3MIB.setRevisions(('2019-11-06 00:00',))
_EltMesIssSnmp3Objects_ObjectIdentity=ObjectIdentity
eltMesIssSnmp3Objects=_EltMesIssSnmp3Objects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,19,1))
_EltMesIssSnmp3Globals_ObjectIdentity=ObjectIdentity
eltMesIssSnmp3Globals=_EltMesIssSnmp3Globals_ObjectIdentity((1,3,6,1,4,1,35265,1,139,19,1,1))
class _EltMesIssWarmStartTrapControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_EltMesIssWarmStartTrapControl_Type.__name__=_A
_EltMesIssWarmStartTrapControl_Object=MibScalar
eltMesIssWarmStartTrapControl=_EltMesIssWarmStartTrapControl_Object((1,3,6,1,4,1,35265,1,139,19,1,1,1),_EltMesIssWarmStartTrapControl_Type())
eltMesIssWarmStartTrapControl.setMaxAccess('read-write')
if mibBuilder.loadTexts:eltMesIssWarmStartTrapControl.setStatus('current')
mibBuilder.exportSymbols('ELTEX-MES-ISS-SNMP3-MIB',**{'eltMesIssSnmp3MIB':eltMesIssSnmp3MIB,'eltMesIssSnmp3Objects':eltMesIssSnmp3Objects,'eltMesIssSnmp3Globals':eltMesIssSnmp3Globals,'eltMesIssWarmStartTrapControl':eltMesIssWarmStartTrapControl})