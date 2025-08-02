_F='bsemErrorMessageRequestId'
_E='bsemErrorMessageAddress'
_D='bsemErrorMessageAddressType'
_C='not-accessible'
_B='BAY-STACK-ERROR-MESSAGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackErrorMessageMib=ModuleIdentity((1,3,6,1,4,1,45,5,19))
if mibBuilder.loadTexts:bayStackErrorMessageMib.setRevisions(('2013-10-11 00:00','2006-11-14 00:00'))
_BsemObjects_ObjectIdentity=ObjectIdentity
bsemObjects=_BsemObjects_ObjectIdentity((1,3,6,1,4,1,45,5,19,1))
_BsemErrorMessageTable_Object=MibTable
bsemErrorMessageTable=_BsemErrorMessageTable_Object((1,3,6,1,4,1,45,5,19,1,1))
if mibBuilder.loadTexts:bsemErrorMessageTable.setStatus(_A)
_BsemErrorMessageEntry_Object=MibTableRow
bsemErrorMessageEntry=_BsemErrorMessageEntry_Object((1,3,6,1,4,1,45,5,19,1,1,1))
bsemErrorMessageEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:bsemErrorMessageEntry.setStatus(_A)
_BsemErrorMessageAddressType_Type=InetAddressType
_BsemErrorMessageAddressType_Object=MibTableColumn
bsemErrorMessageAddressType=_BsemErrorMessageAddressType_Object((1,3,6,1,4,1,45,5,19,1,1,1,1),_BsemErrorMessageAddressType_Type())
bsemErrorMessageAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:bsemErrorMessageAddressType.setStatus(_A)
_BsemErrorMessageAddress_Type=InetAddress
_BsemErrorMessageAddress_Object=MibTableColumn
bsemErrorMessageAddress=_BsemErrorMessageAddress_Object((1,3,6,1,4,1,45,5,19,1,1,1,2),_BsemErrorMessageAddress_Type())
bsemErrorMessageAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bsemErrorMessageAddress.setStatus(_A)
_BsemErrorMessageRequestId_Type=Unsigned32
_BsemErrorMessageRequestId_Object=MibTableColumn
bsemErrorMessageRequestId=_BsemErrorMessageRequestId_Object((1,3,6,1,4,1,45,5,19,1,1,1,3),_BsemErrorMessageRequestId_Type())
bsemErrorMessageRequestId.setMaxAccess(_C)
if mibBuilder.loadTexts:bsemErrorMessageRequestId.setStatus(_A)
_BsemErrorMessageString_Type=DisplayString
_BsemErrorMessageString_Object=MibTableColumn
bsemErrorMessageString=_BsemErrorMessageString_Object((1,3,6,1,4,1,45,5,19,1,1,1,4),_BsemErrorMessageString_Type())
bsemErrorMessageString.setMaxAccess('read-only')
if mibBuilder.loadTexts:bsemErrorMessageString.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bayStackErrorMessageMib':bayStackErrorMessageMib,'bsemObjects':bsemObjects,'bsemErrorMessageTable':bsemErrorMessageTable,'bsemErrorMessageEntry':bsemErrorMessageEntry,_D:bsemErrorMessageAddressType,_E:bsemErrorMessageAddress,_F:bsemErrorMessageRequestId,'bsemErrorMessageString':bsemErrorMessageString})