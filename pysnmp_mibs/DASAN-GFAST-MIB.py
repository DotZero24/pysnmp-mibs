if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dasanEvents,dasanMgmt=mibBuilder.importSymbols('DASAN-SMI','dasanEvents','dasanMgmt')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gFastMIB=ModuleIdentity((1,3,6,1,4,1,6296,9,102))
_GFastTestObj1_ObjectIdentity=ObjectIdentity
gFastTestObj1=_GFastTestObj1_ObjectIdentity((1,3,6,1,4,1,6296,9,102,1))
_GFastTestObj1Temp1_ObjectIdentity=ObjectIdentity
gFastTestObj1Temp1=_GFastTestObj1Temp1_ObjectIdentity((1,3,6,1,4,1,6296,9,102,1,1))
_GFastTestObj1Temp2_ObjectIdentity=ObjectIdentity
gFastTestObj1Temp2=_GFastTestObj1Temp2_ObjectIdentity((1,3,6,1,4,1,6296,9,102,1,2))
_GFastTestObj2_ObjectIdentity=ObjectIdentity
gFastTestObj2=_GFastTestObj2_ObjectIdentity((1,3,6,1,4,1,6296,9,102,2))
_GFastTestObj2Temp1_ObjectIdentity=ObjectIdentity
gFastTestObj2Temp1=_GFastTestObj2Temp1_ObjectIdentity((1,3,6,1,4,1,6296,9,102,2,1))
_GFastTestObj2Temp1Val1_Type=Integer32
_GFastTestObj2Temp1Val1_Object=MibScalar
gFastTestObj2Temp1Val1=_GFastTestObj2Temp1Val1_Object((1,3,6,1,4,1,6296,9,102,2,1,1),_GFastTestObj2Temp1Val1_Type())
gFastTestObj2Temp1Val1.setMaxAccess('read-only')
if mibBuilder.loadTexts:gFastTestObj2Temp1Val1.setStatus('current')
mibBuilder.exportSymbols('DASAN-GFAST-MIB',**{'gFastMIB':gFastMIB,'gFastTestObj1':gFastTestObj1,'gFastTestObj1Temp1':gFastTestObj1Temp1,'gFastTestObj1Temp2':gFastTestObj1Temp2,'gFastTestObj2':gFastTestObj2,'gFastTestObj2Temp1':gFastTestObj2Temp1,'gFastTestObj2Temp1Val1':gFastTestObj2Temp1Val1})