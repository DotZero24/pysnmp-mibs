_C='current'
_B='read-only'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bycast=ModuleIdentity((1,3,6,1,4,1,28669))
if mibBuilder.loadTexts:bycast.setRevisions(('2007-06-07 17:25',))
_Version1_ObjectIdentity=ObjectIdentity
version1=_Version1_ObjectIdentity((1,3,6,1,4,1,28669,1))
_Common_ObjectIdentity=ObjectIdentity
common=_Common_ObjectIdentity((1,3,6,1,4,1,28669,1,0))
_Nmsmi_ObjectIdentity=ObjectIdentity
nmsmi=_Nmsmi_ObjectIdentity((1,3,6,1,4,1,28669,1,0,1))
_System_ObjectIdentity=ObjectIdentity
system=_System_ObjectIdentity((1,3,6,1,4,1,28669,1,0,1,1))
class _Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,11,21,31,41,51,61)));namedValues=NamedValues(*(('unknown',1),('adminDown',11),('normal',21),('notice',31),('minor',41),('major',51),('critical',61)))
_Status_Type.__name__=_A
_Status_Object=MibScalar
status=_Status_Object((1,3,6,1,4,1,28669,1,0,1,1,1),_Status_Type())
status.setMaxAccess(_B)
if mibBuilder.loadTexts:status.setStatus(_C)
_Label_Type=DisplayString
_Label_Object=MibScalar
label=_Label_Object((1,3,6,1,4,1,28669,1,0,1,1,2),_Label_Type())
label.setMaxAccess(_B)
if mibBuilder.loadTexts:label.setStatus(_C)
mibBuilder.exportSymbols('BYCAST-STORAGEGRID-MIB',**{'bycast':bycast,'version1':version1,'common':common,'nmsmi':nmsmi,'system':system,'status':status,'label':label})